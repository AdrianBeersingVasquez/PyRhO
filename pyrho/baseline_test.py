from pyrho import *

print_versions()

for model in ["3", "4", "6"]:
    print(f"Testing model {model}")
    results = run(mods=model, prots="step", sims="Python", plot=False)
    print("OK:", model)
