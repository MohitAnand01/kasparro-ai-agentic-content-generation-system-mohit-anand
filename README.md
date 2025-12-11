
  # 🌟 Kasparro Multi-Agent Content Generation System
  ### Applied AI Engineer Challenge — Official Submission  
  **Author:** Mohit Anand  

  ---

  ## 📌 Overview

  This repository contains a **multi-agent content generation system** built for the Kasparro Applied AI Engineer Challenge.  
  The system transforms a small, fixed product dataset (GlowBoost Vitamin C Serum) into **three structured JSON pages**:

  - `product_page.json`  
  - `faq.json`  
  - `comparison_page.json`

  The architecture follows a **four-agent pipeline**, each with a single responsibility:

  1. **ParserAgent** — Builds internal product models & initializes PageContext  
  2. **QuestionGeneratorAgent** — Produces categorized customer questions  
  3. **ContentPlannerAgent** — Converts questions into FAQ items using logic blocks  
  4. **PageAssemblerAgent** — Uses templates to construct JSON pages  

  This design is deterministic, modular, scalable, and created exactly per assignment specifications.

  ---

  ## 🏗️ System Features

  - ✔ Multi-agent automation pipeline  
  - ✔ Reusable logic blocks (benefits, safety, usage, comparison)  
  - ✔ Custom template engine for JSON generation  
  - ✔ Clean and strict PageContext data modeling  
  - ✔ Zero external dependencies for content generation  
  - ✔ Clean, validated JSON outputs  
  - ✔ Full documentation with diagrams  
  - ✔ Ready for future AI/LLM extensions  

  Full documentation is available at:  
  ➜ `docs/projectdocumentation.md`

  ---

  # 🚀 How to Run This Project Locally

  Follow these steps to run the system on your computer.

  ## 1️⃣ Clone the Repository

  ```bash
  git clone https://github.com/MohitAnand01/kasparro-ai-agentic-content-generation-system-mohit-anand.git
  cd kasparro-ai-agentic-content-generation-system-mohit-anand

   ```

  ## 2️⃣ (Optional) Create a Virtual Environment

  ### Windows:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
  ## 3️⃣ Install Dependencies

  Even though this project has minimal dependencies, install them via:
```bash

pip install -r requirements.txt
```

 ## 4️⃣ Run the Pipeline

Run the orchestrator using:
```bash

python src/main.py
```

  ### After execution, the system will generate output JSON files inside:

  ```text
  outputs/
 
  ├── product_page.json
  ├── faq.json
  └── comparison_page.json
```
## Output Screenshot
## Code Running Succesfully
<img width="946" height="323" alt="image" src="https://github.com/user-attachments/assets/19020a14-fec5-4df6-bad3-f51a8b87eb21" />

 

### Succesfully Getting the Desired Output

## FAQ Page

<img width="1638" height="789" alt="image" src="https://github.com/user-attachments/assets/0fdae4bf-88de-4de6-8201-96b8f96da079" />

## Comparision Page

<img width="1651" height="905" alt="image" src="https://github.com/user-attachments/assets/d56804bf-2c08-4bb7-82a7-93918fcf77d8" />

## Product Page

<img width="1500" height="461" alt="image" src="https://github.com/user-attachments/assets/9a614280-9838-4cb4-849e-c0b46524e263" />





