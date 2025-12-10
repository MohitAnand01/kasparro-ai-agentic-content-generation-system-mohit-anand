# src/main.py
from orchestrator.flow import Orchestrator


def main():
    print("🚀 Starting multi-agent content generation pipeline...")
    orchestrator = Orchestrator(outputs_dir="outputs")
    orchestrator.run()
    print("✅ Pipeline finished. Check the outputs/ folder for JSON files.")


if __name__ == "__main__":
    main()


