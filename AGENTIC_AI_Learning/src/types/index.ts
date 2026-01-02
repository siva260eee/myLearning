/**
 * Type Definitions for Device Financing Agentic AI System
 */

// Agent Configuration Types
export interface AgentConfig {
    id: string;
    name: string;
    model: string;
    trainingData: any[];
    parameters: {
        learningRate: number;
        epochs: number;
        batchSize: number;
    };
}

// Device Information Types
export interface DeviceInfo {
    deviceType: 'Smartphone' | 'Tablet' | 'Laptop' | 'Smartwatch' | 'Other';
    brand: string;
    model: string;
    basePrice: number;
    msrp: number;
    specifications?: DeviceSpecifications;
}

export interface DeviceSpecifications {
    processor?: string;
    ram?: string;
    storage?: string;
    display?: string;
    battery?: string;
    color?: string;
}

// Customer Profile Types
export interface CustomerProfile {
    customerId: string;
    creditScore: number;
    monthlyIncome: number;
    existingDeviceLoans: number;
    preferredPaymentPeriod?: number;
    customerType?: 'individual' | 'business' | 'student' | 'senior';
    accountHistory?: AccountHistory;
}

export interface AccountHistory {
    yearsAsCustomer: number;
    previousPurchases: number;
    paymentHistory: 'excellent' | 'good' | 'fair' | 'poor';
    averageMonthlySpend: number;
}

// Financing Option Types
export interface FinancingOption {
    optionId: string;
    option: string;
    months: number;
    interestRate: number;
    downPayment: number;
    monthlyPayment: number;
    totalCost: number;
    creditScoreRequired: number;
    earlyPayoffPenalty: boolean;
    benefits?: string[];
    restrictions?: string[];
}

// Market Context Types
export interface MarketContext {
    competitorOffers: string[];
    seasonalPromotions: boolean;
    inventoryLevel: 'low' | 'medium' | 'high';
    demandTrend?: 'increasing' | 'stable' | 'decreasing';
    priceHistory?: PriceHistory;
}

export interface PriceHistory {
    currentPrice: number;
    priceOneMonthAgo: number;
    priceThreeMonthsAgo: number;
    priceSixMonthsAgo: number;
}

// Financing Case Types
export interface FinancingCase {
    caseId: string;
    deviceType: string;
    financingOptions: {
        optionId: string;
        description: string;
        monthlyPayment: number;
        totalCost: number;
    }[];
    userScenario: string;
    customer?: CustomerProfile;
    device?: DeviceInfo;
}

export interface ComprehensiveFinancingCase {
    id: number;
    caseTitle: string;
    device: DeviceInfo;
    customer: CustomerProfile;
    userScenario: string;
    financingOptions: FinancingOption[];
    marketContext: MarketContext;
    agentDecisionFactors: string[];
    optimalChoice?: string;
    reasoning?: string;
}

// Agent Decision Types
export interface AgentDecision {
    recommendedOptionId: string;
    confidence: number;
    reasoning: string[];
    alternatives: string[];
    riskFactors: string[];
    customerFitScore: number;
}

// Performance Metrics Types
export interface PerformanceMetrics {
    accuracy: number;
    precision: number;
    recall: number;
    f1Score: number;
    confusionMatrix?: ConfusionMatrix;
}

export interface ConfusionMatrix {
    truePositives: number;
    trueNegatives: number;
    falsePositives: number;
    falseNegatives: number;
}

// Training Data Types
export interface TrainingData {
    input: {
        device: DeviceInfo;
        customer: CustomerProfile;
        scenario: string;
        options: FinancingOption[];
        context: MarketContext;
    };
    expectedOutput: {
        recommendation: string;
        reasoning: string;
        decisionFactors: string[];
    };
}

export interface TrainingResults {
    totalCases: number;
    correctPredictions: number;
    accuracy: number;
    trainingTime: number;
    epochResults: EpochResult[];
}

export interface EpochResult {
    epoch: number;
    loss: number;
    accuracy: number;
    validationAccuracy: number;
}

// API Response Types
export interface ApiResponse<T> {
    success: boolean;
    data?: T;
    error?: ApiError;
    timestamp: Date;
}

export interface ApiError {
    code: string;
    message: string;
    details?: any;
}

// Utility Types
export type CreditScoreRange = 'poor' | 'fair' | 'good' | 'very-good' | 'excellent';
export type DeviceCategory = 'budget' | 'mid-range' | 'premium' | 'flagship';
export type FinancingTerm = 6 | 12 | 18 | 24 | 36;

// Helper function to categorize credit score
export function categorizeCreditScore(score: number): CreditScoreRange {
    if (score < 580) return 'poor';
    if (score < 670) return 'fair';
    if (score < 740) return 'good';
    if (score < 800) return 'very-good';
    return 'excellent';
}

// Helper function to categorize device price
export function categorizeDevice(price: number): DeviceCategory {
    if (price < 300) return 'budget';
    if (price < 800) return 'mid-range';
    if (price < 1500) return 'premium';
    return 'flagship';
}