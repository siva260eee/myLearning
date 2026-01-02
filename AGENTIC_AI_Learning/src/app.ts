/**
 * Device Financing Agentic AI - Express API Server
 * Provides REST endpoints for accessing financing cases and agent recommendations
 */

import express, { Request, Response } from 'express';
import { json } from 'body-parser';
import { DeviceFinancingAgent, AgentConfig } from './agents/index';
import { 
    getDeviceFinancingCases, 
    getFinancingCaseById,
    getFinancingCasesByDeviceType,
    getFinancingCasesByCreditScore,
    exportTrainingData 
} from './device_financing/cases';

const app = express();
const port = process.env.PORT || 3000;

app.use(json());

// Health check endpoint
app.get('/health', (req: Request, res: Response) => {
    res.status(200).json({ status: 'OK', timestamp: new Date() });
});

// Get all device financing cases
app.get('/api/device-financing-cases', (req: Request, res: Response) => {
    try {
        const cases = getDeviceFinancingCases();
        res.status(200).json({
            success: true,
            count: cases.length,
            data: cases
        });
    } catch (error) {
        console.error('Error retrieving financing cases:', error);
        res.status(500).json({ 
            success: false,
            error: 'Failed to retrieve financing cases' 
        });
    }
});

// Get specific case by ID
app.get('/api/device-financing-cases/:id', (req: Request, res: Response) => {
    try {
        const caseId = parseInt(req.params.id);
        const financingCase = getFinancingCaseById(caseId);
        
        if (!financingCase) {
            return res.status(404).json({
                success: false,
                error: `Case with ID ${caseId} not found`
            });
        }
        
        res.status(200).json({
            success: true,
            data: financingCase
        });
    } catch (error) {
        console.error('Error retrieving case:', error);
        res.status(500).json({ 
            success: false,
            error: 'Failed to retrieve case' 
        });
    }
});

// Get cases by device type
app.get('/api/cases/device-type/:type', (req: Request, res: Response) => {
    try {
        const deviceType = req.params.type;
        const cases = getFinancingCasesByDeviceType(deviceType);
        
        res.status(200).json({
            success: true,
            deviceType: deviceType,
            count: cases.length,
            data: cases
        });
    } catch (error) {
        console.error('Error filtering cases:', error);
        res.status(500).json({ 
            success: false,
            error: 'Failed to filter cases by device type' 
        });
    }
});

// Get cases by credit score range
app.get('/api/cases/credit-score/:min/:max', (req: Request, res: Response) => {
    try {
        const minScore = parseInt(req.params.min);
        const maxScore = parseInt(req.params.max);
        
        if (minScore < 300 || maxScore > 850 || minScore > maxScore) {
            return res.status(400).json({
                success: false,
                error: 'Invalid credit score range (must be 300-850, min <= max)'
            });
        }
        
        const cases = getFinancingCasesByCreditScore(minScore, maxScore);
        
        res.status(200).json({
            success: true,
            creditScoreRange: { min: minScore, max: maxScore },
            count: cases.length,
            data: cases
        });
    } catch (error) {
        console.error('Error filtering cases:', error);
        res.status(500).json({ 
            success: false,
            error: 'Failed to filter cases by credit score' 
        });
    }
});

// Analyze a case with an agent
app.post('/api/analyze-case', (req: Request, res: Response) => {
    try {
        const { caseId, agentConfig } = req.body;
        
        if (!caseId) {
            return res.status(400).json({
                success: false,
                error: 'caseId is required'
            });
        }
        
        const financingCase = getFinancingCaseById(caseId);
        
        if (!financingCase) {
            return res.status(404).json({
                success: false,
                error: `Case with ID ${caseId} not found`
            });
        }
        
        // Create agent with provided config or defaults
        const defaultConfig: AgentConfig = {
            agentId: `api-agent-${Date.now()}`,
            name: 'APIAgent',
            modelType: 'rule-based',
            decisionThreshold: 0.7,
            weights: {
                totalCostWeight: 0.25,
                monthlyPaymentWeight: 0.30,
                customerPreferenceWeight: 0.20,
                creditScoreWeight: 0.15,
                termLengthWeight: 0.10
            }
        };
        
        const config = agentConfig ? { ...defaultConfig, ...agentConfig } : defaultConfig;
        const agent = new DeviceFinancingAgent(config);
        
        // Analyze the case
        const decision = agent.analyzeFinancingCase(financingCase);
        
        res.status(200).json({
            success: true,
            caseId: caseId,
            caseTitle: financingCase.caseTitle,
            agentConfig: config,
            recommendation: decision
        });
    } catch (error) {
        console.error('Error analyzing case:', error);
        res.status(500).json({ 
            success: false,
            error: 'Failed to analyze case' 
        });
    }
});

// Train an agent and get performance metrics
app.post('/api/train-agent', (req: Request, res: Response) => {
    try {
        const { agentConfig, trainingCaseIds, testCaseIds } = req.body;
        
        const allCases = getDeviceFinancingCases();
        
        // Use specified cases or default split
        const trainingCases = trainingCaseIds 
            ? trainingCaseIds.map((id: number) => getFinancingCaseById(id)).filter(Boolean)
            : allCases.slice(0, 6);
            
        const testCases = testCaseIds
            ? testCaseIds.map((id: number) => getFinancingCaseById(id)).filter(Boolean)
            : allCases.slice(6);
        
        // Create and train agent
        const config: AgentConfig = agentConfig || {
            agentId: `trained-agent-${Date.now()}`,
            name: 'TrainedAPIAgent',
            modelType: 'hybrid',
            decisionThreshold: 0.75,
            weights: {
                totalCostWeight: 0.25,
                monthlyPaymentWeight: 0.30,
                customerPreferenceWeight: 0.20,
                creditScoreWeight: 0.15,
                termLengthWeight: 0.10
            }
        };
        
        const agent = new DeviceFinancingAgent(config);
        agent.train(trainingCases);
        const metrics = agent.evaluate(testCases);
        
        res.status(200).json({
            success: true,
            agentConfig: config,
            trainingSetSize: trainingCases.length,
            testSetSize: testCases.length,
            metrics: metrics,
            trainingHistory: agent.getTrainingHistory()
        });
    } catch (error) {
        console.error('Error training agent:', error);
        res.status(500).json({ 
            success: false,
            error: 'Failed to train agent' 
        });
    }
});

// Export training data for ML models
app.get('/api/export-training-data', (req: Request, res: Response) => {
    try {
        const trainingData = exportTrainingData();
        
        res.status(200).json({
            success: true,
            data: trainingData
        });
    } catch (error) {
        console.error('Error exporting training data:', error);
        res.status(500).json({ 
            success: false,
            error: 'Failed to export training data' 
        });
    }
});

// Get API documentation
app.get('/api/docs', (req: Request, res: Response) => {
    const documentation = {
        title: 'Device Financing Agentic AI API',
        version: '1.0.0',
        endpoints: [
            {
                method: 'GET',
                path: '/health',
                description: 'Health check endpoint'
            },
            {
                method: 'GET',
                path: '/api/device-financing-cases',
                description: 'Get all financing cases'
            },
            {
                method: 'GET',
                path: '/api/device-financing-cases/:id',
                description: 'Get specific case by ID'
            },
            {
                method: 'GET',
                path: '/api/cases/device-type/:type',
                description: 'Get cases filtered by device type (Smartphone, Tablet, Laptop, Smartwatch)'
            },
            {
                method: 'GET',
                path: '/api/cases/credit-score/:min/:max',
                description: 'Get cases within credit score range (300-850)'
            },
            {
                method: 'POST',
                path: '/api/analyze-case',
                description: 'Analyze a case with an AI agent',
                body: {
                    caseId: 'number (required)',
                    agentConfig: 'AgentConfig (optional)'
                }
            },
            {
                method: 'POST',
                path: '/api/train-agent',
                description: 'Train an agent and evaluate performance',
                body: {
                    agentConfig: 'AgentConfig (optional)',
                    trainingCaseIds: 'number[] (optional)',
                    testCaseIds: 'number[] (optional)'
                }
            },
            {
                method: 'GET',
                path: '/api/export-training-data',
                description: 'Export all cases as training data for ML models'
            }
        ]
    };
    
    res.status(200).json(documentation);
});

// 404 handler
app.use((req: Request, res: Response) => {
    res.status(404).json({
        success: false,
        error: 'Endpoint not found',
        availableEndpoints: '/api/docs'
    });
});

// Start server
app.listen(port, () => {
    console.log('\n╔═══════════════════════════════════════════════════╗');
    console.log('║  Device Financing Agentic AI - Server Running   ║');
    console.log('╚═══════════════════════════════════════════════════╝\n');
    console.log(`🚀 Server: http://localhost:${port}`);
    console.log(`📚 API Docs: http://localhost:${port}/api/docs`);
    console.log(`💊 Health: http://localhost:${port}/health`);
    console.log(`\n📊 Available Cases: ${getDeviceFinancingCases().length}`);
    console.log(`\nReady to serve financing recommendations! 🤖\n`);
});

export default app;