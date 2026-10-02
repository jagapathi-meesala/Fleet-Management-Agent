from pathlib import Path
import re, sys, yaml
ROOT=Path(__file__).resolve().parents[1]
required=["agent.yaml","SOUL.md","README.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md",".env.example",".gitignore","requirements.txt","pytest.ini"]
dirs=["adapters","config","contracts","core","skills","tools","tests","verification"]
def audit():
    errors=[]
    for f in required:
        if not (ROOT/f).is_file(): errors.append(f"missing file: {f}")
    for d in dirs:
        if not (ROOT/d).is_dir(): errors.append(f"missing directory: {d}")
    text=(ROOT/"EXPLAINABILITY.md").read_text() if (ROOT/"EXPLAINABILITY.md").exists() else ""
    headings=["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]
    for h in headings:
        if text.count(h)!=1: errors.append(f"required heading count != 1: {h}")
    for bad in ["## Inputs","## Decision","## Limits"]:
        if re.search(rf"^{re.escape(bad)}$",text,re.M): errors.append(f"conflicting heading: {bad}")
    sections=re.split(r"^## ",text,flags=re.M)[1:]
    for title in ["Inputs and Data Sources","Decision and Reasoning","Limits and Constraints"]:
        sec=next((s for s in sections if s.startswith(title+"\n")),"")
        body=sec.split("\n",1)[1] if "\n" in sec else ""
        sentences=re.findall(r"(?<=[.!?])\s+",body)
        if len(sentences)<1 or sum(1 for c in body if c in '.!?')<2: errors.append(f"section has fewer than two sentences: {title}")
    try:
        m=yaml.safe_load((ROOT/"agent.yaml").read_text())
        if m.get("spec_version")!="0.1.0": errors.append("spec_version is not 0.1.0")
        if m.get("name")!="fleet-management-agent": errors.append("manifest name mismatch")
        for s in m.get("skills",[]):
            if not (ROOT/"skills"/s/"SKILL.md").is_file(): errors.append(f"missing skill: {s}")
        for t in m.get("tools",[]):
            if not (ROOT/"tools"/(t+".py")).is_file(): errors.append(f"missing tool: {t}")
    except Exception as e: errors.append(f"manifest parse error: {e}")
    if errors:
        print("READINESS AUDIT: FAIL"); print("\n".join("- "+e for e in errors)); return 1
    print("READINESS AUDIT: PASS"); return 0
if __name__=="__main__": sys.exit(audit())
