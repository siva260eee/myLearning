#!/usr/bin/env node

/**
 * Quick Demo Runner for Device Financing Agentic AI
 * Run this file to see all demos in action!
 */

const demos = require('./examples/agent_demo');

console.log('\n');
console.log('╔═══════════════════════════════════════════════════════════╗');
console.log('║                                                           ║');
console.log('║   DEVICE FINANCING AGENTIC AI - INTERACTIVE DEMO          ║');
console.log('║                                                           ║');
console.log('║   Demonstrating intelligent AI agents for device         ║');
console.log('║   financing decisions across 8 real-world scenarios      ║');
console.log('║                                                           ║');
console.log('╚═══════════════════════════════════════════════════════════╝');
console.log('\n');

// Run all demos
demos.runAllDemos();

console.log('\n🎓 Want to learn more?');
console.log('   • Read README.md for full documentation');
console.log('   • Follow LEARNING_GUIDE.md for step-by-step tutorials');
console.log('   • Check QUICK_START.md for 5-minute setup');
console.log('   • Review USE_CASES_REFERENCE.md for case details');
console.log('\n🚀 Try the API:');
console.log('   npm start  →  http://localhost:3000');
console.log('\n✨ Happy Learning!\n');
