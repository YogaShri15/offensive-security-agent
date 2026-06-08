from secret_checks import secret_scanner

results = secret_scanner.run()

print("\n")
print("=" * 60)
print("SECRET SCAN REPORT")
print("=" * 60)

for i, finding in enumerate(results, start=1):

    print("\n" + "=" * 60)
    print(f"Finding #{i}")
    print("=" * 60)

    for key, value in finding.items():
        print(f"{key}: {value}")

print("\n")
print(f"Total Findings : {len(results)}")