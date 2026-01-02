/**
 * Device Financing Cases for Agentic AI Learning
 * Comprehensive scenarios for training AI agents on device financing decisions
 */

export interface DeviceInfo {
    deviceType: string;
    brand: string;
    model: string;
    basePrice: number;
    msrp: number;
}

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
}

export interface CustomerProfile {
    customerId: string;
    creditScore: number;
    monthlyIncome: number;
    existingDeviceLoans: number;
    preferredPaymentPeriod?: number;
}

export interface FinancingCase {
    id: number;
    caseTitle: string;
    device: DeviceInfo;
    customer: CustomerProfile;
    userScenario: string;
    financingOptions: FinancingOption[];
    marketContext: {
        competitorOffers: string[];
        seasonalPromotions: boolean;
        inventoryLevel: string;
    };
    agentDecisionFactors: string[];
    optimalChoice?: string;
    reasoning?: string;
}

/**
 * Calculate monthly payment for a financing option
 */
function calculateMonthlyPayment(
    principal: number,
    interestRate: number,
    months: number,
    downPayment: number
): number {
    const loanAmount = principal - downPayment;
    if (interestRate === 0) {
        return loanAmount / months;
    }
    const monthlyRate = interestRate / 12;
    return (loanAmount * monthlyRate * Math.pow(1 + monthlyRate, months)) / 
           (Math.pow(1 + monthlyRate, months) - 1);
}

/**
 * Calculate total cost including interest
 */
function calculateTotalCost(
    principal: number,
    interestRate: number,
    months: number,
    downPayment: number
): number {
    const monthlyPayment = calculateMonthlyPayment(principal, interestRate, months, downPayment);
    return (monthlyPayment * months) + downPayment;
}

/**
 * Generate comprehensive device financing cases for AI agent training
 */
export function getDeviceFinancingCases(): FinancingCase[] {
    const cases: FinancingCase[] = [
        // Case 1: Premium Smartphone - Excellent Credit
        {
            id: 1,
            caseTitle: "Premium Smartphone Financing - High Credit Score Customer",
            device: {
                deviceType: "Smartphone",
                brand: "Apple",
                model: "iPhone 15 Pro Max",
                basePrice: 1199,
                msrp: 1199
            },
            customer: {
                customerId: "CUST-001",
                creditScore: 780,
                monthlyIncome: 6500,
                existingDeviceLoans: 0,
                preferredPaymentPeriod: 24
            },
            userScenario: "Customer wants to purchase latest iPhone with best available terms. Has excellent credit and stable income.",
            financingOptions: [
                {
                    optionId: "OPT-1A",
                    option: "0% APR 12-month financing",
                    months: 12,
                    interestRate: 0.0,
                    downPayment: 0,
                    monthlyPayment: 99.92,
                    totalCost: 1199,
                    creditScoreRequired: 720,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-1B",
                    option: "0% APR 24-month financing",
                    months: 24,
                    interestRate: 0.0,
                    downPayment: 0,
                    monthlyPayment: 49.96,
                    totalCost: 1199,
                    creditScoreRequired: 700,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-1C",
                    option: "36-month financing with 5% APR",
                    months: 36,
                    interestRate: 0.05,
                    downPayment: 200,
                    monthlyPayment: 29.89,
                    totalCost: 1276,
                    creditScoreRequired: 680,
                    earlyPayoffPenalty: true
                }
            ],
            marketContext: {
                competitorOffers: ["Samsung offering 0% for 18 months", "Google Pixel with $200 trade-in bonus"],
                seasonalPromotions: true,
                inventoryLevel: "high"
            },
            agentDecisionFactors: [
                "Customer credit score qualifies for all options",
                "Monthly income supports higher monthly payments",
                "Customer preference for 24-month term aligns with 0% APR option",
                "No early payoff penalty on recommended option",
                "Seasonal promotion available"
            ],
            optimalChoice: "OPT-1B",
            reasoning: "0% APR 24-month option matches customer preference while minimizing total cost. Customer's excellent credit qualifies for best terms."
        },

        // Case 2: Mid-Range Smartphone - Average Credit with Trade-In
        {
            id: 2,
            caseTitle: "Mid-Range Smartphone with Trade-In - Average Credit",
            device: {
                deviceType: "Smartphone",
                brand: "Samsung",
                model: "Galaxy S24",
                basePrice: 799,
                msrp: 899
            },
            customer: {
                customerId: "CUST-002",
                creditScore: 650,
                monthlyIncome: 3800,
                existingDeviceLoans: 1,
                preferredPaymentPeriod: 18
            },
            userScenario: "Customer trading in old phone (worth $150) and needs affordable monthly payment. Average credit score.",
            financingOptions: [
                {
                    optionId: "OPT-2A",
                    option: "18-month with 8% APR + Trade-In Credit",
                    months: 18,
                    interestRate: 0.08,
                    downPayment: 150,
                    monthlyPayment: 39.67,
                    totalCost: 864,
                    creditScoreRequired: 620,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-2B",
                    option: "24-month with 12% APR + Trade-In Credit",
                    months: 24,
                    interestRate: 0.12,
                    downPayment: 150,
                    monthlyPayment: 30.71,
                    totalCost: 887,
                    creditScoreRequired: 600,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-2C",
                    option: "12-month with 6% APR + Trade-In Credit",
                    months: 12,
                    interestRate: 0.06,
                    downPayment: 150,
                    monthlyPayment: 56.13,
                    totalCost: 824,
                    creditScoreRequired: 660,
                    earlyPayoffPenalty: false
                }
            ],
            marketContext: {
                competitorOffers: ["AT&T offering $200 off with new line", "Verizon 0% for qualified customers"],
                seasonalPromotions: false,
                inventoryLevel: "medium"
            },
            agentDecisionFactors: [
                "Customer has one existing device loan (debt-to-income consideration)",
                "Credit score limits access to best rates",
                "Monthly payment affordability is key factor (~10% of monthly income)",
                "Trade-in value reduces principal amount",
                "Customer preference for 18-month term available"
            ],
            optimalChoice: "OPT-2A",
            reasoning: "18-month option balances customer preference with affordable monthly payment of $39.67. Lower total interest cost than 24-month option while monthly payment remains manageable."
        },

        // Case 3: Tablet Purchase for Business - Corporate Account
        {
            id: 3,
            caseTitle: "Business Tablet Fleet Purchase - Corporate Account",
            device: {
                deviceType: "Tablet",
                brand: "Apple",
                model: "iPad Pro 12.9-inch",
                basePrice: 1099,
                msrp: 1099
            },
            customer: {
                customerId: "CORP-001",
                creditScore: 800,
                monthlyIncome: 50000,
                existingDeviceLoans: 5,
                preferredPaymentPeriod: 12
            },
            userScenario: "Corporate customer purchasing 10 tablets for sales team. Needs quick deployment and flexible terms.",
            financingOptions: [
                {
                    optionId: "OPT-3A",
                    option: "Bulk 0% APR 12-month (10 devices)",
                    months: 12,
                    interestRate: 0.0,
                    downPayment: 1000,
                    monthlyPayment: 908.33,
                    totalCost: 10990,
                    creditScoreRequired: 750,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-3B",
                    option: "Business Line of Credit - 24-month 4% APR",
                    months: 24,
                    interestRate: 0.04,
                    downPayment: 0,
                    monthlyPayment: 477.82,
                    totalCost: 11467,
                    creditScoreRequired: 720,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-3C",
                    option: "Lease-to-Own Program - 36-month",
                    months: 36,
                    interestRate: 0.06,
                    downPayment: 500,
                    monthlyPayment: 319.44,
                    totalCost: 11990,
                    creditScoreRequired: 700,
                    earlyPayoffPenalty: true
                }
            ],
            marketContext: {
                competitorOffers: ["Microsoft Surface with enterprise discount", "Samsung offering MDM solution included"],
                seasonalPromotions: true,
                inventoryLevel: "high"
            },
            agentDecisionFactors: [
                "Corporate account with excellent credit",
                "Bulk purchase qualifies for special pricing",
                "Cash flow management important for business",
                "Tax implications of purchase vs lease",
                "Need for warranty and support services",
                "Upgrade cycle considerations"
            ],
            optimalChoice: "OPT-3A",
            reasoning: "0% APR 12-month option with minimal down payment provides lowest total cost. Quick payoff timeline aligns with corporate preference and technology refresh cycle. No early payoff penalty allows flexibility."
        },

        // Case 4: Budget Smartphone - Low Credit Score
        {
            id: 4,
            caseTitle: "Budget Smartphone - Credit-Challenged Customer",
            device: {
                deviceType: "Smartphone",
                brand: "Google",
                model: "Pixel 7a",
                basePrice: 449,
                msrp: 499
            },
            customer: {
                customerId: "CUST-004",
                creditScore: 580,
                monthlyIncome: 2400,
                existingDeviceLoans: 2,
                preferredPaymentPeriod: 24
            },
            userScenario: "Customer with limited credit history needs affordable smartphone. Has two existing device payment plans.",
            financingOptions: [
                {
                    optionId: "OPT-4A",
                    option: "24-month with 18% APR",
                    months: 24,
                    interestRate: 0.18,
                    downPayment: 100,
                    monthlyPayment: 17.63,
                    totalCost: 523,
                    creditScoreRequired: 550,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-4B",
                    option: "12-month with 15% APR + Higher Down Payment",
                    months: 12,
                    interestRate: 0.15,
                    downPayment: 150,
                    monthlyPayment: 26.89,
                    totalCost: 473,
                    creditScoreRequired: 580,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-4C",
                    option: "Secured Financing 18-month 10% APR",
                    months: 18,
                    interestRate: 0.10,
                    downPayment: 200,
                    monthlyPayment: 15.31,
                    totalCost: 476,
                    creditScoreRequired: 540,
                    earlyPayoffPenalty: false
                }
            ],
            marketContext: {
                competitorOffers: ["Carrier offering phone with service contract", "Buy-here-pay-here options with higher rates"],
                seasonalPromotions: false,
                inventoryLevel: "low"
            },
            agentDecisionFactors: [
                "Low credit score limits financing options",
                "Multiple existing device loans increase risk",
                "Monthly income constrains payment capacity",
                "Need to build credit history",
                "Higher down payment reduces monthly burden",
                "Affordability is primary concern"
            ],
            optimalChoice: "OPT-4C",
            reasoning: "Secured financing offers best balance: lowest monthly payment ($15.31), moderate total cost, and helps build credit. Customer can afford down payment to reduce monthly obligation while maintaining existing device payments."
        },

        // Case 5: Gaming Laptop - Student with Cosigner
        {
            id: 5,
            caseTitle: "Gaming Laptop - Student Financing with Cosigner",
            device: {
                deviceType: "Laptop",
                brand: "ASUS",
                model: "ROG Strix G16",
                basePrice: 1699,
                msrp: 1899
            },
            customer: {
                customerId: "CUST-005",
                creditScore: 620,
                monthlyIncome: 1200,
                existingDeviceLoans: 0,
                preferredPaymentPeriod: 24
            },
            userScenario: "College student needs gaming laptop for game development coursework. Parent willing to cosign. Limited personal income but has part-time job.",
            financingOptions: [
                {
                    optionId: "OPT-5A",
                    option: "Student 0% APR 18-month (with cosigner)",
                    months: 18,
                    interestRate: 0.0,
                    downPayment: 300,
                    monthlyPayment: 77.72,
                    totalCost: 1699,
                    creditScoreRequired: 600,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-5B",
                    option: "Extended 36-month with 7% APR",
                    months: 36,
                    interestRate: 0.07,
                    downPayment: 200,
                    monthlyPayment: 46.33,
                    totalCost: 1868,
                    creditScoreRequired: 620,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-5C",
                    option: "Deferred Payment - 6 months + 24-month 5% APR",
                    months: 24,
                    interestRate: 0.05,
                    downPayment: 400,
                    monthlyPayment: 57.34,
                    totalCost: 1776,
                    creditScoreRequired: 640,
                    earlyPayoffPenalty: false
                }
            ],
            marketContext: {
                competitorOffers: ["Dell offering student discount", "Best Buy student rewards program", "Back-to-school promotions active"],
                seasonalPromotions: true,
                inventoryLevel: "high"
            },
            agentDecisionFactors: [
                "Cosigner significantly improves financing terms",
                "Student status qualifies for special 0% program",
                "Limited income requires careful affordability analysis",
                "Seasonal back-to-school promotions available",
                "Long-term value for coursework justifies investment",
                "Potential for payment assistance from family"
            ],
            optimalChoice: "OPT-5A",
            reasoning: "Student 0% APR program with cosigner offers best value: no interest charges, 18-month term is manageable, monthly payment of $77.72 is high but feasible with parent support. Saves $169 vs next best option while paying off faster."
        },

        // Case 6: Smart Watch - Existing Customer Upgrade
        {
            id: 6,
            caseTitle: "Smartwatch Upgrade - Loyal Customer Early Upgrade",
            device: {
                deviceType: "Smartwatch",
                brand: "Apple",
                model: "Apple Watch Ultra 2",
                basePrice: 799,
                msrp: 799
            },
            customer: {
                customerId: "CUST-006",
                creditScore: 720,
                monthlyIncome: 5200,
                existingDeviceLoans: 1,
                preferredPaymentPeriod: 12
            },
            userScenario: "Existing customer with 6 months remaining on current device. Wants to upgrade to latest smartwatch model. Has been customer for 5 years.",
            financingOptions: [
                {
                    optionId: "OPT-6A",
                    option: "Early Upgrade 0% APR 12-month (loyalty bonus)",
                    months: 12,
                    interestRate: 0.0,
                    downPayment: 0,
                    monthlyPayment: 66.58,
                    totalCost: 799,
                    creditScoreRequired: 680,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-6B",
                    option: "Trade-In + 0% APR 18-month",
                    months: 18,
                    interestRate: 0.0,
                    downPayment: 100,
                    monthlyPayment: 38.83,
                    totalCost: 799,
                    creditScoreRequired: 700,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-6C",
                    option: "Rollover existing + New 24-month plan",
                    months: 24,
                    interestRate: 0.03,
                    downPayment: 50,
                    monthlyPayment: 32.73,
                    totalCost: 836,
                    creditScoreRequired: 680,
                    earlyPayoffPenalty: true
                }
            ],
            marketContext: {
                competitorOffers: ["Samsung offering $150 trade-in for any smartwatch", "Garmin with free accessories bundle"],
                seasonalPromotions: false,
                inventoryLevel: "medium"
            },
            agentDecisionFactors: [
                "Long-term customer loyalty merits best available terms",
                "Good credit score qualifies for premium options",
                "Existing device loan means debt management consideration",
                "Customer preference for 12-month payoff",
                "Trade-in value of current device available",
                "Customer retention strategy important"
            ],
            optimalChoice: "OPT-6A",
            reasoning: "Loyalty bonus 0% APR 12-month option rewards long-term customer, no down payment needed, matches customer preference for quick payoff, and maintains positive customer relationship. Highest monthly payment but customer income supports it."
        },

        // Case 7: Budget Tablet - Senior Citizen First-Time Buyer
        {
            id: 7,
            caseTitle: "Budget Tablet - Senior First-Time Technology Purchase",
            device: {
                deviceType: "Tablet",
                brand: "Amazon",
                model: "Fire HD 10",
                basePrice: 149,
                msrp: 149
            },
            customer: {
                customerId: "CUST-007",
                creditScore: 750,
                monthlyIncome: 2800,
                existingDeviceLoans: 0,
                preferredPaymentPeriod: 6
            },
            userScenario: "Senior citizen purchasing first tablet for video calls with family. Wants simplest payment option and concerned about affordability.",
            financingOptions: [
                {
                    optionId: "OPT-7A",
                    option: "6-month 0% APR Senior Discount",
                    months: 6,
                    interestRate: 0.0,
                    downPayment: 0,
                    monthlyPayment: 24.83,
                    totalCost: 149,
                    creditScoreRequired: 650,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-7B",
                    option: "Full Payment with 15% Senior Discount",
                    months: 0,
                    interestRate: 0.0,
                    downPayment: 127,
                    monthlyPayment: 0,
                    totalCost: 127,
                    creditScoreRequired: 0,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-7C",
                    option: "12-month 0% APR",
                    months: 12,
                    interestRate: 0.0,
                    downPayment: 0,
                    monthlyPayment: 12.42,
                    totalCost: 149,
                    creditScoreRequired: 600,
                    earlyPayoffPenalty: false
                }
            ],
            marketContext: {
                competitorOffers: ["Walmart offering similar tablet for $119", "Senior center has group purchase program"],
                seasonalPromotions: true,
                inventoryLevel: "high"
            },
            agentDecisionFactors: [
                "Senior citizen discount applicable",
                "Low price point makes financing optional",
                "Excellent credit score not typically primary factor for seniors",
                "Preference for simple, straightforward payment",
                "Fixed income considerations",
                "Tech support and ease of use more important than financing terms"
            ],
            optimalChoice: "OPT-7B",
            reasoning: "Full payment with 15% senior discount provides best value ($127 vs $149), eliminates monthly payment concerns, and simplifies the purchase. Customer's excellent credit and fixed income make one-time payment preferable to managing monthly bills."
        },

        // Case 8: Premium Laptop - Freelancer Business Purchase
        {
            id: 8,
            caseTitle: "Premium Laptop - Freelancer Business Expense",
            device: {
                deviceType: "Laptop",
                brand: "Apple",
                model: "MacBook Pro 16-inch M3 Max",
                basePrice: 3499,
                msrp: 3499
            },
            customer: {
                customerId: "CUST-008",
                creditScore: 690,
                monthlyIncome: 4500,
                existingDeviceLoans: 0,
                preferredPaymentPeriod: 24
            },
            userScenario: "Freelance video editor needs high-performance laptop for 4K video editing. Business expense with potential tax deduction. Income variable but consistent.",
            financingOptions: [
                {
                    optionId: "OPT-8A",
                    option: "Business 0% APR 12-month",
                    months: 12,
                    interestRate: 0.0,
                    downPayment: 500,
                    monthlyPayment: 249.92,
                    totalCost: 3499,
                    creditScoreRequired: 720,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-8B",
                    option: "24-month 6% APR with Business Rewards",
                    months: 24,
                    interestRate: 0.06,
                    downPayment: 350,
                    monthlyPayment: 139.44,
                    totalCost: 3697,
                    creditScoreRequired: 680,
                    earlyPayoffPenalty: false
                },
                {
                    optionId: "OPT-8C",
                    option: "36-month 8% APR Business Line",
                    months: 36,
                    interestRate: 0.08,
                    downPayment: 300,
                    monthlyPayment: 100.57,
                    totalCost: 3920,
                    creditScoreRequired: 660,
                    earlyPayoffPenalty: false
                }
            ],
            marketContext: {
                competitorOffers: ["Dell Precision with similar specs", "Lenovo ThinkPad P series with business support", "Educational pricing available if enrolled in courses"],
                seasonalPromotions: false,
                inventoryLevel: "medium"
            },
            agentDecisionFactors: [
                "Business purchase qualifies for tax deduction",
                "Credit score slightly below 0% APR threshold",
                "Variable income requires affordable monthly payment",
                "High-value purchase needs careful cash flow management",
                "Business rewards program offers future benefits",
                "Equipment depreciation schedule aligns with financing term"
            ],
            optimalChoice: "OPT-8B",
            reasoning: "24-month option balances affordability ($139.44/month) with reasonable total cost increase ($198 over 2 years). Customer qualifies with 690 credit score, monthly payment manageable with variable income, and 24-month term aligns with typical business equipment depreciation."
        }
    ];

    return cases;
}

/**
 * Get a specific financing case by ID
 */
export function getFinancingCaseById(id: number): FinancingCase | undefined {
    const cases = getDeviceFinancingCases();
    return cases.find(c => c.id === id);
}

/**
 * Filter cases by device type
 */
export function getFinancingCasesByDeviceType(deviceType: string): FinancingCase[] {
    const cases = getDeviceFinancingCases();
    return cases.filter(c => c.device.deviceType.toLowerCase() === deviceType.toLowerCase());
}

/**
 * Filter cases by credit score range
 */
export function getFinancingCasesByCreditScore(minScore: number, maxScore: number): FinancingCase[] {
    const cases = getDeviceFinancingCases();
    return cases.filter(c => c.customer.creditScore >= minScore && c.customer.creditScore <= maxScore);
}

/**
 * Export all cases as training data for AI agents
 */
export function exportTrainingData(): any {
    const cases = getDeviceFinancingCases();
    return {
        totalCases: cases.length,
        cases: cases.map(c => ({
            input: {
                device: c.device,
                customer: c.customer,
                scenario: c.userScenario,
                options: c.financingOptions,
                context: c.marketContext
            },
            expectedOutput: {
                recommendation: c.optimalChoice,
                reasoning: c.reasoning,
                decisionFactors: c.agentDecisionFactors
            }
        }))
    };
}