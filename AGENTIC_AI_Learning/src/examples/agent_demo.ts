/**
 * Device Financing Agent Demo
 * Demonstrates how to use the agentic AI system for device financing decisions
 */

import { DeviceFinancingAgent } from '../agents/index';
import { 
    getDeviceFinancingCases, 
    getFinancingCaseById,
    getFinancingCasesByDeviceType,
    getFinancingCasesByCreditScore,
    exportTrainingData
} from '../device_financing/cases';

/**
 * Demo 1: Basic Agent Usage
 */
export function demo1_BasicAgentUsage(): void {
    console.log('\n═══════════════════════════════════════════════════');
    console.log('Demo 1: Basic Agent Usage');
    console.log('═══════════════════════════════════════════════════\n');

    // Create a new agent
    const agent = new DeviceFinancingAgent({
        agentId: 'agent-001',
        name: 'BasicFinancingAgent',
        modelType: 'rule-based',
        decisionThreshold: 0.7,
        weights: {
            totalCostWeight: 0.25,
            monthlyPaymentWeight: 0.30,
            customerPreferenceWeight: 0.20,
            creditScoreWeight: 0.15,
            termLengthWeight: 0.10
        }
    });

    // Get a sample case
    const sampleCase = getFinancingCaseById(1);
    
    if (sampleCase) {
        console.log(`\n📋 Analyzing Case: ${sampleCase.caseTitle}`);
        console.log(`   Device: ${sampleCase.device.brand} ${sampleCase.device.model}`);
        console.log(`   Price: $${sampleCase.device.basePrice}`);
        console.log(`   Customer Credit Score: ${sampleCase.customer.creditScore}`);
        console.log(`   Monthly Income: $${sampleCase.customer.monthlyIncome}`);
        
        // Analyze the case
        const decision = agent.analyzeFinancingCase(sampleCase);
        
        // Display results
        console.log(`\n🎯 Agent Decision:`);
        console.log(`   Recommended: ${decision.recommendedOptionId}`);
        console.log(`   Confidence: ${decision.confidence.toFixed(2)}%`);
        console.log(`   Customer Fit Score: ${decision.customerFitScore.toFixed(2)}`);
        
        console.log(`\n💡 Reasoning:`);
        decision.reasoning.forEach(reason => console.log(`   • ${reason}`));
        
        if (decision.riskFactors.length > 0) {
            console.log(`\n⚠️  Risk Factors:`);
            decision.riskFactors.forEach(risk => console.log(`   • ${risk}`));
        }
        
        if (decision.alternatives.length > 0) {
            console.log(`\n🔄 Alternative Options: ${decision.alternatives.join(', ')}`);
        }
    }
}

/**
 * Demo 2: Training the Agent
 */
export function demo2_TrainingAgent(): void {
    console.log('\n═══════════════════════════════════════════════════');
    console.log('Demo 2: Training the Agent');
    console.log('═══════════════════════════════════════════════════\n');

    // Create agent with custom weights
    const agent = new DeviceFinancingAgent({
        agentId: 'agent-002',
        name: 'TrainedFinancingAgent',
        modelType: 'hybrid',
        decisionThreshold: 0.75,
        learningRate: 0.01,
        weights: {
            totalCostWeight: 0.30,
            monthlyPaymentWeight: 0.35,
            customerPreferenceWeight: 0.15,
            creditScoreWeight: 0.10,
            termLengthWeight: 0.10
        }
    });

    // Get all cases for training
    const allCases = getDeviceFinancingCases();
    
    // Split into training and test sets (80/20 split)
    const splitIndex = Math.floor(allCases.length * 0.8);
    const trainingCases = allCases.slice(0, splitIndex);
    const testCases = allCases.slice(splitIndex);

    console.log(`Total Cases: ${allCases.length}`);
    console.log(`Training Set: ${trainingCases.length} cases`);
    console.log(`Test Set: ${testCases.length} cases\n`);

    // Train the agent
    agent.train(trainingCases);

    // Evaluate on test set
    const metrics = agent.evaluate(testCases);

    // Display training history
    const history = agent.getTrainingHistory();
    console.log(`\n📚 Training History:`);
    history.forEach((session, index) => {
        console.log(`   Session ${index + 1}:`);
        console.log(`      Cases: ${session.casesCount}`);
        console.log(`      Accuracy: ${session.accuracy.toFixed(2)}%`);
        console.log(`      Time: ${session.trainingTime}ms`);
    });
}

/**
 * Demo 3: Analyzing Multiple Cases by Category
 */
export function demo3_CategoryAnalysis(): void {
    console.log('\n═══════════════════════════════════════════════════');
    console.log('Demo 3: Analyzing Cases by Category');
    console.log('═══════════════════════════════════════════════════\n');

    const agent = new DeviceFinancingAgent({
        agentId: 'agent-003',
        name: 'CategoryAnalyzer',
        modelType: 'rule-based',
        decisionThreshold: 0.7
    });

    // Analyze all smartphone cases
    console.log('📱 SMARTPHONE CASES:\n');
    const smartphoneCases = getFinancingCasesByDeviceType('Smartphone');
    
    smartphoneCases.forEach(phoneCase => {
        const decision = agent.analyzeFinancingCase(phoneCase);
        console.log(`   ${phoneCase.caseTitle}`);
        console.log(`      → ${decision.recommendedOptionId} (${decision.confidence.toFixed(0)}% confidence)`);
    });

    // Analyze all tablet cases
    console.log('\n💻 TABLET CASES:\n');
    const tabletCases = getFinancingCasesByDeviceType('Tablet');
    
    tabletCases.forEach(tabletCase => {
        const decision = agent.analyzeFinancingCase(tabletCase);
        console.log(`   ${tabletCase.caseTitle}`);
        console.log(`      → ${decision.recommendedOptionId} (${decision.confidence.toFixed(0)}% confidence)`);
    });

    // Analyze all laptop cases
    console.log('\n💻 LAPTOP CASES:\n');
    const laptopCases = getFinancingCasesByDeviceType('Laptop');
    
    laptopCases.forEach(laptopCase => {
        const decision = agent.analyzeFinancingCase(laptopCase);
        console.log(`   ${laptopCase.caseTitle}`);
        console.log(`      → ${decision.recommendedOptionId} (${decision.confidence.toFixed(0)}% confidence)`);
    });
}

/**
 * Demo 4: Credit Score Based Analysis
 */
export function demo4_CreditScoreAnalysis(): void {
    console.log('\n═══════════════════════════════════════════════════');
    console.log('Demo 4: Credit Score Based Analysis');
    console.log('═══════════════════════════════════════════════════\n');

    const agent = new DeviceFinancingAgent({
        agentId: 'agent-004',
        name: 'CreditAnalyzer',
        modelType: 'rule-based',
        decisionThreshold: 0.7
    });

    // Define credit score ranges
    const creditRanges = [
        { name: 'Excellent (740+)', min: 740, max: 850 },
        { name: 'Good (670-739)', min: 670, max: 739 },
        { name: 'Fair (580-669)', min: 580, max: 669 }
    ];

    creditRanges.forEach(range => {
        console.log(`\n💳 ${range.name}:\n`);
        const cases = getFinancingCasesByCreditScore(range.min, range.max);
        
        if (cases.length === 0) {
            console.log('   No cases found in this range');
            return;
        }

        cases.forEach(creditCase => {
            const decision = agent.analyzeFinancingCase(creditCase);
            const qualifyingOptions = creditCase.financingOptions.filter(
                opt => creditCase.customer.creditScore >= opt.creditScoreRequired
            );
            
            console.log(`   ${creditCase.caseTitle}`);
            console.log(`      Score: ${creditCase.customer.creditScore}`);
            console.log(`      Qualifying Options: ${qualifyingOptions.length}/${creditCase.financingOptions.length}`);
            console.log(`      Recommended: ${decision.recommendedOptionId}`);
            
            if (decision.riskFactors.length > 0) {
                console.log(`      Risks: ${decision.riskFactors.length} factor(s) identified`);
            }
        });
    });
}

/**
 * Demo 5: Export Training Data
 */
export function demo5_ExportTrainingData(): void {
    console.log('\n═══════════════════════════════════════════════════');
    console.log('Demo 5: Export Training Data');
    console.log('═══════════════════════════════════════════════════\n');

    const trainingData = exportTrainingData();
    
    console.log(`📊 Training Data Export:`);
    console.log(`   Total Cases: ${trainingData.totalCases}`);
    console.log(`\n   Sample Case Structure:`);
    
    if (trainingData.cases.length > 0) {
        const sample = trainingData.cases[0];
        console.log(`   Input Fields:`);
        console.log(`      • device: ${Object.keys(sample.input.device).join(', ')}`);
        console.log(`      • customer: ${Object.keys(sample.input.customer).join(', ')}`);
        console.log(`      • options: ${sample.input.options.length} financing options`);
        console.log(`      • context: ${Object.keys(sample.input.context).join(', ')}`);
        console.log(`\n   Output Fields:`);
        console.log(`      • recommendation: ${sample.expectedOutput.recommendation}`);
        console.log(`      • reasoning: ${sample.expectedOutput.reasoning ? 'Yes' : 'No'}`);
        console.log(`      • decisionFactors: ${sample.expectedOutput.decisionFactors.length} factors`);
    }

    console.log(`\n   This data can be used to train ML models for device financing decisions.`);
}

/**
 * Demo 6: Comparing Multiple Agents
 */
export function demo6_AgentComparison(): void {
    console.log('\n═══════════════════════════════════════════════════');
    console.log('Demo 6: Comparing Multiple Agents');
    console.log('═══════════════════════════════════════════════════\n');

    // Create three agents with different strategies
    const conservativeAgent = new DeviceFinancingAgent({
        agentId: 'conservative',
        name: 'ConservativeAgent',
        modelType: 'rule-based',
        decisionThreshold: 0.8,
        weights: {
            totalCostWeight: 0.40,  // Prioritize low cost
            monthlyPaymentWeight: 0.30,
            customerPreferenceWeight: 0.10,
            creditScoreWeight: 0.15,
            termLengthWeight: 0.05
        }
    });

    const affordabilityAgent = new DeviceFinancingAgent({
        agentId: 'affordability',
        name: 'AffordabilityAgent',
        modelType: 'rule-based',
        decisionThreshold: 0.7,
        weights: {
            totalCostWeight: 0.15,
            monthlyPaymentWeight: 0.45,  // Prioritize low monthly payment
            customerPreferenceWeight: 0.20,
            creditScoreWeight: 0.10,
            termLengthWeight: 0.10
        }
    });

    const balancedAgent = new DeviceFinancingAgent({
        agentId: 'balanced',
        name: 'BalancedAgent',
        modelType: 'hybrid',
        decisionThreshold: 0.75,
        weights: {
            totalCostWeight: 0.25,
            monthlyPaymentWeight: 0.25,
            customerPreferenceWeight: 0.25,
            creditScoreWeight: 0.15,
            termLengthWeight: 0.10
        }
    });

    const testCase = getFinancingCaseById(2);  // Mid-range smartphone case
    
    if (testCase) {
        console.log(`📋 Test Case: ${testCase.caseTitle}\n`);
        
        const agents = [conservativeAgent, affordabilityAgent, balancedAgent];
        
        agents.forEach(agent => {
            const decision = agent.analyzeFinancingCase(testCase);
            console.log(`\n🤖 ${agent.getPerformanceMetrics().totalDecisions === 1 ? agent.exportState().config.name : 'Unknown'}:`);
            console.log(`   Recommendation: ${decision.recommendedOptionId}`);
            console.log(`   Confidence: ${decision.confidence.toFixed(2)}%`);
            console.log(`   Top Reason: ${decision.reasoning[0]}`);
        });
    }
}

/**
 * Run all demos
 */
export function runAllDemos(): void {
    console.log('\n\n');
    console.log('╔═══════════════════════════════════════════════════╗');
    console.log('║  DEVICE FINANCING AGENTIC AI - DEMO SUITE       ║');
    console.log('╚═══════════════════════════════════════════════════╝');

    demo1_BasicAgentUsage();
    demo2_TrainingAgent();
    demo3_CategoryAnalysis();
    demo4_CreditScoreAnalysis();
    demo5_ExportTrainingData();
    demo6_AgentComparison();

    console.log('\n\n');
    console.log('╔═══════════════════════════════════════════════════╗');
    console.log('║  ALL DEMOS COMPLETED                             ║');
    console.log('╚═══════════════════════════════════════════════════╝\n');
}

// Export individual demos
export default {
    demo1_BasicAgentUsage,
    demo2_TrainingAgent,
    demo3_CategoryAnalysis,
    demo4_CreditScoreAnalysis,
    demo5_ExportTrainingData,
    demo6_AgentComparison,
    runAllDemos
};
