/**
 * Test Suite for Device Financing Agent
 * Comprehensive tests for agentic AI functionality
 */

import { DeviceFinancingAgent } from '../agents/index';
import { 
    getDeviceFinancingCases, 
    getFinancingCaseById,
    FinancingCase 
} from '../device_financing/cases';

describe('Device Financing Agent Tests', () => {
    let agent: DeviceFinancingAgent;

    beforeEach(() => {
        agent = new DeviceFinancingAgent({
            agentId: 'test-agent-001',
            name: 'TestAgent',
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
    });

    describe('Agent Initialization', () => {
        test('should create agent with valid configuration', () => {
            expect(agent).toBeDefined();
            const state = agent.exportState();
            expect(state.config.agentId).toBe('test-agent-001');
            expect(state.config.name).toBe('TestAgent');
        });

        test('should initialize with empty performance metrics', () => {
            const metrics = agent.getPerformanceMetrics();
            expect(metrics.totalDecisions).toBe(0);
            expect(metrics.correctDecisions).toBe(0);
            expect(metrics.accuracy).toBe(0);
        });
    });

    describe('Case Analysis', () => {
        test('should analyze premium smartphone case correctly', () => {
            const testCase = getFinancingCaseById(1);
            expect(testCase).toBeDefined();

            if (testCase) {
                const decision = agent.analyzeFinancingCase(testCase);
                
                expect(decision).toBeDefined();
                expect(decision.recommendedOptionId).toBeTruthy();
                expect(decision.confidence).toBeGreaterThanOrEqual(0);
                expect(decision.confidence).toBeLessThanOrEqual(100);
                expect(decision.reasoning).toBeInstanceOf(Array);
                expect(decision.reasoning.length).toBeGreaterThan(0);
            }
        });

        test('should recommend 0% APR option for excellent credit', () => {
            const testCase = getFinancingCaseById(1);  // Excellent credit case
            
            if (testCase) {
                const decision = agent.analyzeFinancingCase(testCase);
                const recommendedOption = testCase.financingOptions.find(
                    opt => opt.optionId === decision.recommendedOptionId
                );
                
                expect(recommendedOption).toBeDefined();
                // Should prefer 0% APR for excellent credit
                expect(recommendedOption?.interestRate).toBe(0);
            }
        });

        test('should handle low credit score appropriately', () => {
            const testCase = getFinancingCaseById(4);  // Low credit score case
            
            if (testCase) {
                const decision = agent.analyzeFinancingCase(testCase);
                
                expect(decision).toBeDefined();
                expect(decision.riskFactors.length).toBeGreaterThan(0);
                // Should identify credit-related risks
                const hasCreditRisk = decision.riskFactors.some(
                    risk => risk.toLowerCase().includes('credit')
                );
                expect(hasCreditRisk).toBe(true);
            }
        });

        test('should consider monthly income affordability', () => {
            const testCase = getFinancingCaseById(2);  // Average credit case
            
            if (testCase) {
                const decision = agent.analyzeFinancingCase(testCase);
                const recommendedOption = testCase.financingOptions.find(
                    opt => opt.optionId === decision.recommendedOptionId
                );
                
                if (recommendedOption && testCase.customer) {
                    const paymentRatio = recommendedOption.monthlyPayment / testCase.customer.monthlyIncome;
                    // Monthly payment should be reasonable (< 20% of income)
                    expect(paymentRatio).toBeLessThan(0.20);
                }
            }
        });

        test('should respect customer payment period preference', () => {
            const testCase = getFinancingCaseById(1);
            
            if (testCase && testCase.customer.preferredPaymentPeriod) {
                const decision = agent.analyzeFinancingCase(testCase);
                const recommendedOption = testCase.financingOptions.find(
                    opt => opt.optionId === decision.recommendedOptionId
                );
                
                // If customer has a preference and it's available at 0% APR, should match
                const hasPreferredTerm = testCase.financingOptions.some(
                    opt => opt.months === testCase.customer.preferredPaymentPeriod && opt.interestRate === 0
                );
                
                if (hasPreferredTerm && recommendedOption) {
                    expect(recommendedOption.months).toBe(testCase.customer.preferredPaymentPeriod);
                }
            }
        });

        test('should provide multiple reasoning points', () => {
            const testCase = getFinancingCaseById(1);
            
            if (testCase) {
                const decision = agent.analyzeFinancingCase(testCase);
                expect(decision.reasoning.length).toBeGreaterThanOrEqual(3);
            }
        });

        test('should identify risk factors when present', () => {
            const testCase = getFinancingCaseById(4);  // Low credit case
            
            if (testCase) {
                const decision = agent.analyzeFinancingCase(testCase);
                expect(decision.riskFactors.length).toBeGreaterThan(0);
            }
        });

        test('should handle business/corporate cases differently', () => {
            const testCase = getFinancingCaseById(3);  // Corporate case
            
            if (testCase) {
                const decision = agent.analyzeFinancingCase(testCase);
                
                expect(decision).toBeDefined();
                expect(decision.confidence).toBeGreaterThan(70);
                // Corporate cases typically have higher confidence due to better credit
            }
        });
    });

    describe('Training and Evaluation', () => {
        test('should train on multiple cases', () => {
            const cases = getDeviceFinancingCases();
            const trainingCases = cases.slice(0, 5);
            
            agent.train(trainingCases);
            
            const history = agent.getTrainingHistory();
            expect(history.length).toBeGreaterThan(0);
            expect(history[0].casesCount).toBe(5);
            expect(history[0].accuracy).toBeGreaterThanOrEqual(0);
        });

        test('should improve accuracy with training', () => {
            const cases = getDeviceFinancingCases();
            
            agent.train(cases);
            
            const metrics = agent.getPerformanceMetrics();
            expect(metrics.totalDecisions).toBe(cases.length);
            expect(metrics.accuracy).toBeGreaterThan(0);
        });

        test('should evaluate performance on test cases', () => {
            const cases = getDeviceFinancingCases();
            const testCases = cases.slice(0, 3);
            
            const metrics = agent.evaluate(testCases);
            
            expect(metrics).toBeDefined();
            expect(metrics.totalDecisions).toBe(3);
            expect(metrics.accuracy).toBeGreaterThanOrEqual(0);
            expect(metrics.averageConfidence).toBeGreaterThan(0);
        });

        test('should track decision logs', () => {
            const testCase = getFinancingCaseById(1);
            
            if (testCase) {
                agent.analyzeFinancingCase(testCase);
                
                const metrics = agent.getPerformanceMetrics();
                expect(metrics.totalDecisions).toBe(1);
            }
        });
    });

    describe('Agent Configuration', () => {
        test('should update agent configuration', () => {
            agent.updateConfig({
                decisionThreshold: 0.85
            });
            
            const state = agent.exportState();
            expect(state.config.decisionThreshold).toBe(0.85);
        });

        test('should export complete agent state', () => {
            const testCase = getFinancingCaseById(1);
            if (testCase) {
                agent.analyzeFinancingCase(testCase);
            }
            
            const state = agent.exportState();
            
            expect(state).toBeDefined();
            expect(state.config).toBeDefined();
            expect(state.performanceMetrics).toBeDefined();
            expect(state.trainingHistory).toBeDefined();
        });
    });

    describe('Edge Cases', () => {
        test('should handle customer with no qualifying options', () => {
            // Create a test case with very low credit score
            const edgeCase: FinancingCase = {
                id: 999,
                caseTitle: "Edge Case - No Qualifying Options",
                device: {
                    deviceType: "Smartphone",
                    brand: "Test",
                    model: "TestPhone",
                    basePrice: 500,
                    msrp: 500
                },
                customer: {
                    customerId: "EDGE-001",
                    creditScore: 400,  // Very low
                    monthlyIncome: 1500,
                    existingDeviceLoans: 3
                },
                userScenario: "Edge case for testing",
                financingOptions: [
                    {
                        optionId: "OPT-EDGE-1",
                        option: "12-month 0% APR",
                        months: 12,
                        interestRate: 0,
                        downPayment: 0,
                        monthlyPayment: 41.67,
                        totalCost: 500,
                        creditScoreRequired: 700,  // Too high
                        earlyPayoffPenalty: false
                    }
                ],
                marketContext: {
                    competitorOffers: [],
                    seasonalPromotions: false,
                    inventoryLevel: "medium"
                },
                agentDecisionFactors: ["Test factor"]
            };

            const decision = agent.analyzeFinancingCase(edgeCase);
            
            expect(decision).toBeDefined();
            expect(decision.recommendedOptionId).toBe('NONE');
            expect(decision.confidence).toBe(0);
            expect(decision.reasoning.length).toBeGreaterThan(0);
        });

        test('should handle cases with existing device loans', () => {
            const testCase = getFinancingCaseById(2);  // Has existing loans
            
            if (testCase) {
                const decision = agent.analyzeFinancingCase(testCase);
                
                expect(decision).toBeDefined();
                // Should mention existing loans in risk factors
                const hasDebtWarning = decision.riskFactors.some(
                    risk => risk.toLowerCase().includes('loan')
                );
                expect(hasDebtWarning).toBe(true);
            }
        });
    });

    describe('Performance Metrics', () => {
        test('should calculate accuracy correctly', () => {
            const cases = getDeviceFinancingCases();
            const testCases = cases.slice(0, 4);
            
            agent.evaluate(testCases);
            
            const metrics = agent.getPerformanceMetrics();
            const expectedAccuracy = (metrics.correctDecisions / metrics.totalDecisions) * 100;
            
            expect(metrics.accuracy).toBeCloseTo(expectedAccuracy, 2);
        });

        test('should track average confidence', () => {
            const cases = getDeviceFinancingCases();
            agent.evaluate(cases.slice(0, 3));
            
            const metrics = agent.getPerformanceMetrics();
            expect(metrics.averageConfidence).toBeGreaterThan(0);
            expect(metrics.averageConfidence).toBeLessThanOrEqual(100);
        });
    });
});

describe('Device Financing Cases Tests', () => {
    test('should retrieve all cases', () => {
        const cases = getDeviceFinancingCases();
        expect(cases).toBeInstanceOf(Array);
        expect(cases.length).toBeGreaterThan(0);
    });

    test('should retrieve specific case by ID', () => {
        const testCase = getFinancingCaseById(1);
        expect(testCase).toBeDefined();
        expect(testCase?.id).toBe(1);
    });

    test('should return undefined for non-existent case ID', () => {
        const testCase = getFinancingCaseById(9999);
        expect(testCase).toBeUndefined();
    });

    test('all cases should have required fields', () => {
        const cases = getDeviceFinancingCases();
        
        cases.forEach(testCase => {
            expect(testCase.id).toBeDefined();
            expect(testCase.caseTitle).toBeDefined();
            expect(testCase.device).toBeDefined();
            expect(testCase.customer).toBeDefined();
            expect(testCase.financingOptions).toBeDefined();
            expect(testCase.financingOptions.length).toBeGreaterThan(0);
        });
    });

    test('all financing options should have valid data', () => {
        const cases = getDeviceFinancingCases();
        
        cases.forEach(testCase => {
            testCase.financingOptions.forEach(option => {
                expect(option.optionId).toBeTruthy();
                expect(option.months).toBeGreaterThan(0);
                expect(option.interestRate).toBeGreaterThanOrEqual(0);
                expect(option.totalCost).toBeGreaterThanOrEqual(testCase.device.basePrice - option.downPayment);
            });
        });
    });
});
