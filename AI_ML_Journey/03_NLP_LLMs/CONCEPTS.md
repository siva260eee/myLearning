# Natural Language Processing & Large Language Models

## Overview
NLP focuses on enabling computers to understand, interpret, and generate human language. LLMs represent the cutting edge of this field, capable of sophisticated language understanding and generation.

## Part 1: NLP Fundamentals

### 1. Text Preprocessing

#### Tokenization
- **Word tokenization**: Split text into words
- **Sentence tokenization**: Split into sentences
- **Subword tokenization**: BPE, WordPiece, SentencePiece

#### Text Cleaning
- Lowercase conversion
- Removing punctuation
- Removing stop words
- Stemming vs Lemmatization

#### Example:
```python
Text: "The cats are running fast!"
Tokens: ["The", "cats", "are", "running", "fast", "!"]
Lowercase: ["the", "cats", "are", "running", "fast", "!"]
Stop words removed: ["cats", "running", "fast"]
Lemmatized: ["cat", "run", "fast"]
```

### 2. Text Representation

#### Bag of Words (BoW)
- Count word occurrences
- Loses word order
- Sparse representation

#### TF-IDF (Term Frequency-Inverse Document Frequency)
```
TF-IDF = (count of word in document / total words) × 
         log(total documents / documents containing word)
```
- Weighs important words higher
- Reduces common word importance

#### Word Embeddings
**Word2Vec**
- CBOW (Continuous Bag of Words)
- Skip-gram
- Captures semantic relationships
- Similar words have similar vectors

**GloVe (Global Vectors)**
- Based on word co-occurrence matrix
- Combines global statistics

**FastText**
- Considers subwords
- Better for rare words
- Handles out-of-vocabulary words

### 3. Sequence Models for NLP

#### RNNs for Text
- Process sequences
- Maintain context
- Problems: vanishing gradients

#### LSTMs for Text
- Better long-term dependencies
- Forget/input/output gates
- Popular for machine translation

#### GRUs
- Simpler than LSTM
- Fewer parameters
- Often similar performance

### 4. Attention Mechanism

#### Why Attention?
- Focus on relevant parts
- Solve long sequence problem
- No fixed-size encoding

#### Self-Attention
```
Attention(Q, K, V) = softmax(QK^T / √d_k)V
```
- Query (Q): What I'm looking for
- Key (K): What I have
- Value (V): What I give
- Computes relevance scores

## Part 2: Transformers

### 1. Transformer Architecture

#### Core Components

**Multi-Head Attention**
- Multiple attention mechanisms in parallel
- Learn different aspects of relationships
- Combine results

**Positional Encoding**
- Add position information
- Since attention has no inherent order
- Sine/cosine functions

**Feed-Forward Networks**
- After attention
- Two linear layers with ReLU
- Applied to each position

**Layer Normalization**
- Stabilize training
- Faster convergence

#### Encoder-Decoder Structure

**Encoder**
- Process input sequence
- Multi-head self-attention
- Feed-forward network
- Multiple layers stacked

**Decoder**
- Generate output sequence
- Masked self-attention (can't see future)
- Encoder-decoder attention
- Feed-forward network

### 2. Transformer Variants

#### BERT (Bidirectional Encoder Representations from Transformers)
- **Type**: Encoder-only
- **Training**: Masked Language Modeling (MLM)
- **Use**: Understanding tasks
  - Text classification
  - Named Entity Recognition
  - Question answering
  - Sentiment analysis

**Key Features**:
- Bidirectional context
- Pre-trained on massive data
- Fine-tune for specific tasks

#### GPT (Generative Pre-trained Transformer)
- **Type**: Decoder-only
- **Training**: Autoregressive (predict next word)
- **Use**: Generation tasks
  - Text completion
  - Creative writing
  - Code generation
  - Chatbots

**Evolution**:
- GPT-1: 117M parameters
- GPT-2: 1.5B parameters
- GPT-3: 175B parameters
- GPT-4: Multimodal, even larger

#### T5 (Text-to-Text Transfer Transformer)
- **Type**: Encoder-decoder
- **Approach**: Everything as text-to-text
- **Versatile**: Translation, summarization, Q&A

#### Other Important Models
- **RoBERTa**: Optimized BERT training
- **ALBERT**: Lighter BERT
- **DistilBERT**: Smaller, faster BERT
- **XLNet**: Permutation language modeling
- **ELECTRA**: More efficient pre-training

## Part 3: Large Language Models (LLMs)

### 1. What are LLMs?

#### Characteristics
- Billions of parameters (100B+)
- Trained on massive text corpora
- Emergent capabilities
- Few-shot/zero-shot learning
- General purpose

#### Scaling Laws
- More parameters → Better performance
- More data → Better performance
- More compute → Better performance
- But: diminishing returns and costs

### 2. Key LLMs

#### GPT Series (OpenAI)
- **GPT-3.5**: ChatGPT base
- **GPT-4**: Multimodal, reasoning
- **Capabilities**:
  - Conversation
  - Code generation
  - Complex reasoning
  - Creative writing

#### Claude (Anthropic)
- Constitutional AI
- Focus on safety and helpfulness
- Long context windows
- Strong reasoning

#### PaLM (Google)
- 540B parameters
- Strong math and reasoning
- Multilingual

#### LLaMA (Meta)
- Open weights
- Efficient architecture
- Community fine-tunes (Alpaca, Vicuna)

#### Gemini (Google)
- Multimodal from ground up
- Multiple sizes (Ultra, Pro, Nano)
- Competes with GPT-4

### 3. LLM Training Process

#### Pre-training
1. **Objective**: Predict next token
2. **Data**: Massive text corpus (web, books)
3. **Scale**: Weeks/months on thousands of GPUs
4. **Result**: General language understanding

#### Fine-tuning
1. **Supervised Fine-Tuning (SFT)**
   - Task-specific data
   - Instruction following
   
2. **Reinforcement Learning from Human Feedback (RLHF)**
   - Human rankings
   - Reward model
   - PPO optimization
   - Aligns with human preferences

### 4. Prompt Engineering

#### Basic Prompting
```
Simple: "Translate to French: Hello"
Result: "Bonjour"
```

#### Few-Shot Learning
```
Example 1: Input → Output
Example 2: Input → Output
Example 3: Input → Output
New: Input → ?
```

#### Chain-of-Thought (CoT)
```
Problem: Math word problem
Response: Let's think step by step:
1. First, we identify...
2. Then, we calculate...
3. Finally, we get...
```

#### Advanced Techniques
- **Zero-shot CoT**: "Let's think step by step"
- **Self-consistency**: Multiple reasoning paths
- **Tree of thoughts**: Explore multiple branches
- **ReAct**: Reasoning + Acting

### 5. LLM Capabilities

#### Reasoning
- Mathematical problem solving
- Logical deduction
- Planning and strategy

#### Knowledge
- Factual question answering
- Explanations
- Synthesis of information

#### Generation
- Creative writing
- Code generation
- Data analysis
- Content creation

#### Understanding
- Sentiment analysis
- Intent classification
- Entity extraction
- Summarization

### 6. LLM Limitations

#### Hallucinations
- Generate plausible but incorrect information
- Confident false statements
- Mitigation: retrieval augmentation, citations

#### Knowledge Cutoff
- Training data has end date
- No real-time information
- Solution: Internet search integration

#### Context Window
- Limited input length
- GPT-3.5: 4K tokens
- GPT-4: 8K-128K tokens
- Claude: 100K-200K tokens

#### Biases
- Training data biases
- Social and cultural biases
- Requires careful monitoring

## Part 4: Working with LLMs

### 1. API Access

#### OpenAI API
```python
import openai

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

#### Anthropic Claude
```python
import anthropic

client = anthropic.Client(api_key="...")
response = client.messages.create(
    model="claude-3-opus-20240229",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### 2. Open Source LLMs

#### Hugging Face Transformers
```python
from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')
result = generator("Hello, I am")
```

#### Local LLMs
- **LLaMA.cpp**: Run LLaMA locally
- **Ollama**: Easy local deployment
- **GPT4All**: Desktop LLMs
- **LM Studio**: GUI for local LLMs

### 3. Fine-tuning LLMs

#### LoRA (Low-Rank Adaptation)
- Efficient fine-tuning
- Few trainable parameters
- Preserve base model

#### QLoRA
- Quantized LoRA
- Even more efficient
- 4-bit quantization

### 4. Retrieval Augmented Generation (RAG)

#### Concept
```
User Query → Retrieve Relevant Docs → LLM + Context → Answer
```

#### Components
1. **Vector Database**: Store embeddings
2. **Retriever**: Find relevant docs
3. **LLM**: Generate answer with context

#### Benefits
- Up-to-date information
- Reduce hallucinations
- Domain-specific knowledge
- Citations and sources

### 5. LLM Applications

#### Chatbots
- Customer service
- Personal assistants
- Educational tutors

#### Content Creation
- Writing assistance
- Marketing copy
- Code generation

#### Analysis
- Document summarization
- Sentiment analysis
- Data extraction

#### Agents
- Task automation
- Research assistants
- Workflow orchestration

## Part 5: Embeddings

### 1. What are Embeddings?

#### Definition
- Dense vector representations
- Capture semantic meaning
- Similar concepts → Similar vectors

#### Properties
- Fixed dimensions (384, 768, 1536, etc.)
- Can be compared (cosine similarity)
- Used for search, clustering, classification

### 2. Embedding Models

#### OpenAI Embeddings
- text-embedding-3-small
- text-embedding-3-large
- High quality, API-based

#### Open Source
- **sentence-transformers**
- **BGE models**
- **E5 models**
- **instructor models**

### 3. Applications

#### Semantic Search
- Find similar documents
- Better than keyword search
- Understanding intent

#### Clustering
- Group similar items
- Topic discovery
- Organization

#### Recommendation Systems
- Similar products
- Content recommendations
- Personalization

## Part 6: Evaluation

### 1. LLM Evaluation Metrics

#### Perplexity
- How surprised model is
- Lower is better
- Good for comparing models

#### BLEU Score
- Machine translation
- N-gram overlap
- Reference-based

#### ROUGE Score
- Summarization
- Recall-oriented
- Multiple variants

#### Human Evaluation
- Quality ratings
- Preference rankings
- Most reliable but expensive

### 2. Benchmarks

#### MMLU (Massive Multitask Language Understanding)
- 57 subjects
- Knowledge and reasoning

#### HellaSwag
- Common sense reasoning

#### HumanEval
- Code generation

#### TruthfulQA
- Factual accuracy
- Resist misinformation

## Next Steps

1. Work through examples
2. Complete exercises
3. Experiment with APIs
4. Build RAG system
5. Move to AI Agents module

## Resources

- Hugging Face Courses
- OpenAI Cookbook
- Attention Is All You Need (paper)
- LangChain Documentation
- LlamaIndex Documentation
- Papers with Code (NLP section)
