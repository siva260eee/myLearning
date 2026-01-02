/**
 * Device Financing Agent - Agentic AI Implementation
 * Intelligent agent for analyzing and recommending optimal device financing options
 */

import { FinancingCase, FinancingOption, CustomerProfile, DeviceInfo } from '../device_financing/cases';

export interface AgentConfig {
    agentId: string;
    name: string;
    modelType: 'rule-based' | 'ml-based' | 'hybrid';
    decisionThreshold: number;
    learningRate?: number;
    weights?: DecisionWeights;
}

export interface DecisionWeights {
    totalCostWeight: number;
    monthlyPaymentWeight: number;
    customerPreferenceWeight: number;
    creditScoreWeight: number;
    termLengthWeight: number;
}

export interface AgentDecision {
    recommendedOptionId: string;
    confidence: number;
    reasoning: string[];
    alternatives: string[];
    riskFactors: string[];
    customerFitScore: number;
}

export interface AgentPerformanceMetrics {
    totalDecisions: number;
    correctDecisions: number;
    accuracy: number;
    averageConfidence: number;
    decisionsLog: DecisionLog[];
}

export interface DecisionLog {
    caseId: number;
    timestamp: Date;
    decision: AgentDecision;
    actualOptimal?: string;
    wasCorrect?: boolean;
}

/**
 * Main Device Financing Agent Class
 */
export class DeviceFinancingAgent {
    private config: AgentConfig;
    private performanceMetrics: AgentPerformanceMetrics;
    private trainingHistory: any[];

    constructor(config: AgentConfig) {
        this.config = config;
        this.performanceMetrics = {
            totalDecisions: 0,
            correctDecisions: 0,
            accuracy: 0,
            averageConfidence: 0,
            decisionsLog: []
        };
        this.trainingHistory = [];
    }

    /**
     * Analyze a financing case and make a recommendation
     */
    public analyzeFinancingCase(financingCase: FinancingCase): AgentDecision {
        console.log(`\n🤖 Agent ${this.config.name} analyzing case: ${financingCase.caseTitle}`);

        // Step 1: Filter qualifying options based on credit score
        const qualifyingOptions = this.filterQualifyingOptions(
            financingCase.financingOptions,
            financingCase.customer.creditScore
        );

        if (qualifyingOptions.length === 0) {
            return this.createNoQualificationDecision(financingCase);
        }

        // Step 2: Score each option
        const scoredOptions = qualifyingOptions.map(option => ({
            option,
            score: this.scoreFinancingOption(option, financingCase.customer, financingCase.device)
        }));

        // Step 3: Rank options by score
        scoredOptions.sort((a, b) => b.score - a.score);

        // Step 4: Build decision with reasoning
        const decision = this.buildDecision(scoredOptions, financingCase);

        // Step 5: Log decision
        this.logDecision(financingCase.id, decision, financingCase.optimalChoice);

        return decision;
    }

    /**
     * Filter options customer qualifies for based on credit score
     */
    private filterQualifyingOptions(
        options: FinancingOption[],
        creditScore: number
    ): FinancingOption[] {
        return options.filter(opt => creditScore >= opt.creditScoreRequired);
    }

    /**
     * Score a financing option based on multiple factors
     */
    private scoreFinancingOption(
        option: FinancingOption,
        customer: CustomerProfile,
        device: DeviceInfo
    ): number {
        const weights = this.config.weights || this.getDefaultWeights();

        // Factor 1: Total cost efficiency (lower is better)
        const costScore = (1 - (option.totalCost - device.basePrice) / device.basePrice) * 100;

        // Factor 2: Monthly payment affordability (should be < 15% of monthly income)
        const paymentRatio = option.monthlyPayment / customer.monthlyIncome;
        const affordabilityScore = paymentRatio < 0.10 ? 100 : 
                                   paymentRatio < 0.15 ? 80 : 
                                   paymentRatio < 0.20 ? 60 : 40;

        // Factor 3: Term length preference
        const termPreferenceScore = customer.preferredPaymentPeriod 
            ? (100 - Math.abs(option.months - customer.preferredPaymentPeriod) * 5)
            : 70;

        // Factor 4: Interest rate (lower is better)
        const interestScore = (1 - option.interestRate) * 100;

        // Factor 5: No early payoff penalty bonus
        const penaltyBonus = option.earlyPayoffPenalty ? 0 : 20;

        // Weighted score
        const totalScore = (
            (costScore * weights.totalCostWeight) +
            (affordabilityScore * weights.monthlyPaymentWeight) +
            (termPreferenceScore * weights.customerPreferenceWeight) +
            (interestScore * 0.15) +
            penaltyBonus
        );

        return totalScore;
    }

    /**
     * Build final decision with reasoning
     */
    private buildDecision(
        scoredOptions: Array<{ option: FinancingOption; score: number }>,
        financingCase: FinancingCase
    ): AgentDecision {
        const topOption = scoredOptions[0];
        const reasoning: string[] = [];

        // Build reasoning
        reasoning.push(`Selected ${topOption.option.option} (${topOption.option.optionId})`);
        reasoning.push(`Total cost: $${topOption.option.totalCost.toFixed(2)}`);
        reasoning.push(`Monthly payment: $${topOption.option.monthlyPayment.toFixed(2)} (${((topOption.option.monthlyPayment / financingCase.customer.monthlyIncome) * 100).toFixed(1)}% of monthly income)`);
        
        if (topOption.option.interestRate === 0) {
            reasoning.push(`✅ 0% APR - No interest charges`);
        } else {
            reasoning.push(`Interest rate: ${(topOption.option.interestRate * 100).toFixed(1)}% APR`);
        }

        if (!topOption.option.earlyPayoffPenalty) {
            reasoning.push(`✅ No early payoff penalty - Flexible repayment`);
        }

        if (financingCase.customer.preferredPaymentPeriod === topOption.option.months) {
            reasoning.push(`✅ Matches customer's preferred ${topOption.option.months}-month term`);
        }

        // Risk factors
        const riskFactors: string[] = [];
        const paymentRatio = topOption.option.monthlyPayment / financingCase.customer.monthlyIncome;
        
        if (paymentRatio > 0.15) {
            riskFactors.push(`⚠️ Monthly payment is ${(paymentRatio * 100).toFixed(1)}% of income (>15% threshold)`);
        }

        if (financingCase.customer.existingDeviceLoans > 0) {
            riskFactors.push(`⚠️ Customer has ${financingCase.customer.existingDeviceLoans} existing device loan(s)`);
        }

        if (financingCase.customer.creditScore < 650) {
            riskFactors.push(`⚠️ Below-average credit score may limit future financing options`);
        }

        // Calculate confidence
        const confidence = Math.min(95, Math.max(60, topOption.score));

        return {
            recommendedOptionId: topOption.option.optionId,
            confidence: confidence,
            reasoning: reasoning,
            alternatives: scoredOptions.slice(1, 3).map(opt => opt.option.optionId),
            riskFactors: riskFactors,
            customerFitScore: topOption.score
        };
    }

    /**
     * Create decision when customer doesn't qualify for any options
     */
    private createNoQualificationDecision(financingCase: FinancingCase): AgentDecision {
        return {
            recommendedOptionId: 'NONE',
            confidence: 0,
            reasoning: [
                `Customer credit score (${financingCase.customer.creditScore}) does not qualify for any available options`,
                `Minimum required: ${Math.min(...financingCase.financingOptions.map(opt => opt.creditScoreRequired))}`,
                'Recommendation: Consider secured financing or co-signer options'
            ],
            alternatives: [],
            riskFactors: ['Credit score below all option thresholds'],
            customerFitScore: 0
        };
    }

    /**
     * Train agent with historical cases
     */
    public train(trainingCases: FinancingCase[]): void {
        console.log(`\n🎓 Training ${this.config.name} with ${trainingCases.length} cases...`);
        
        const startTime = Date.now();
        let correctPredictions = 0;

        trainingCases.forEach((trainingCase, index) => {
            const decision = this.analyzeFinancingCase(trainingCase);
            
            if (decision.recommendedOptionId === trainingCase.optimalChoice) {
                correctPredictions++;
            }

            // Log training progress
            if ((index + 1) % 5 === 0 || index === trainingCases.length - 1) {
                const accuracy = (correctPredictions / (index + 1)) * 100;
                console.log(`  Progress: ${index + 1}/${trainingCases.length} cases - Accuracy: ${accuracy.toFixed(1)}%`);
            }
        });

        const trainingTime = Date.now() - startTime;
        const accuracy = (correctPredictions / trainingCases.length) * 100;

        this.trainingHistory.push({
            timestamp: new Date(),
            casesCount: trainingCases.length,
            accuracy: accuracy,
            trainingTime: trainingTime
        });

        console.log(`\n✅ Training complete!`);
        console.log(`   Final Accuracy: ${accuracy.toFixed(2)}%`);
        console.log(`   Training Time: ${trainingTime}ms`);
        console.log(`   Correct: ${correctPredictions}/${trainingCases.length}`);
    }

    /**
     * Evaluate agent performance on test cases
     */
    public evaluate(testCases: FinancingCase[]): AgentPerformanceMetrics {
        console.log(`\n📊 Evaluating ${this.config.name} on ${testCases.length} test cases...`);

        let correctDecisions = 0;
        let totalConfidence = 0;

        testCases.forEach(testCase => {
            const decision = this.analyzeFinancingCase(testCase);
            const isCorrect = decision.recommendedOptionId === testCase.optimalChoice;
            
            if (isCorrect) correctDecisions++;
            totalConfidence += decision.confidence;

            this.performanceMetrics.decisionsLog.push({
                caseId: testCase.id,
                timestamp: new Date(),
                decision: decision,
                actualOptimal: testCase.optimalChoice,
                wasCorrect: isCorrect
            });
        });

        this.performanceMetrics.totalDecisions = testCases.length;
        this.performanceMetrics.correctDecisions = correctDecisions;
        this.performanceMetrics.accuracy = (correctDecisions / testCases.length) * 100;
        this.performanceMetrics.averageConfidence = totalConfidence / testCases.length;

        console.log(`\n📈 Evaluation Results:`);
        console.log(`   Accuracy: ${this.performanceMetrics.accuracy.toFixed(2)}%`);
        console.log(`   Correct: ${correctDecisions}/${testCases.length}`);
        console.log(`   Avg Confidence: ${this.performanceMetrics.averageConfidence.toFixed(2)}%`);

        return this.performanceMetrics;
    }

    /**
     * Get default decision weights
     */
    private getDefaultWeights(): DecisionWeights {
        return {
            totalCostWeight: 0.25,
            monthlyPaymentWeight: 0.30,
            customerPreferenceWeight: 0.20,
            creditScoreWeight: 0.15,
            termLengthWeight: 0.10
        };
    }

    /**
     * Log a decision for performance tracking
     */
    private logDecision(caseId: number, decision: AgentDecision, actualOptimal?: string): void {
        this.performanceMetrics.totalDecisions++;
        
        if (actualOptimal && decision.recommendedOptionId === actualOptimal) {
            this.performanceMetrics.correctDecisions++;
        }

        this.performanceMetrics.accuracy = 
            (this.performanceMetrics.correctDecisions / this.performanceMetrics.totalDecisions) * 100;
    }

    /**
     * Get performance metrics
     */
    public getPerformanceMetrics(): AgentPerformanceMetrics {
        return this.performanceMetrics;
    }

    /**
     * Get training history
     */
    public getTrainingHistory(): any[] {
        return this.trainingHistory;
    }

    /**
     * Update agent configuration
     */
    public updateConfig(newConfig: Partial<AgentConfig>): void {
        this.config = { ...this.config, ...newConfig };
        console.log(`Agent configuration updated:`, this.config);
    }

    /**
     * Export agent state for saving/loading
     */
    public exportState(): any {
        return {
            config: this.config,
            performanceMetrics: this.performanceMetrics,
            trainingHistory: this.trainingHistory
        };
    }
}

export default DeviceFinancingAgent;