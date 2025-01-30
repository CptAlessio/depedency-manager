# Copyright 2025 Alessio Marziali
import json
import sys
import time
from typing import List, Dict
from modules.npmjs import npmjs_get_license
from modules.mvnrepository import mvnrepository_get_license

# Set to true to scan using NPMJS
scanNPMJS = True

# Set to true to scan using Maven Repository
scanMavenRepository = True

# Set to true to scan dev dependencies
scanDevDependencies = False

# throttle the requests to 0.5 seconds
throttle = 0.5

## function to parse package.json and return the dependencies
def parse_package_json_dependencies(package_json_path: str) -> Dict[str, List[str]]:
    try:
        with open(package_json_path, 'r') as file:
            package_data = json.load(file)

        # Extract dependencies
        dependencies = []
        if 'dependencies' in package_data:
            dependencies = [
                # remove the version from the dependency
                f"{pkg}" 
                for pkg, version in package_data['dependencies'].items()
            ]
            
        # Extract dev dependencies
        dev_dependencies = []

        if scanDevDependencies:
            if 'devDependencies' in package_data:
                dev_dependencies = [
                    f"{pkg}@{version.strip('^')}" 
                    for pkg, version in package_data['devDependencies'].items()
                ]
            
        return {
            'dependencies': dependencies,
            'dev_dependencies': dev_dependencies
        }
        
    except FileNotFoundError:
        print(f"Error: Could not find {package_json_path}")
        return {'dependencies': [], 'dev_dependencies': []}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {package_json_path}")
        return {'dependencies': [], 'dev_dependencies': []}
    
# __main__ to run the script
if __name__ == "__main__":
    if len(sys.argv) > 1:
        package_json_path = sys.argv[1];
    else:
        print("No package.json path provided. Using default: package.json");
        sys.exit(1)
    
    # list of dependencies
    deps = parse_package_json_dependencies(package_json_path)
    
    print("\nDependencies:")
    for dep in deps['dependencies']:
        if scanNPMJS:
            license = npmjs_get_license(dep)
            print(f" NPMJS - {dep} license: {license}")
    
        if scanMavenRepository:
            license = mvnrepository_get_license(dep)
            print(f" Maven Repository - {dep} license: {license}")


        if scanNPMJS or scanMavenRepository:
            # wait 0.5 seconds before checking the next dependency
            time.sleep(throttle)

    if scanDevDependencies:
        print("\nDev Dependencies:")
        for dep in deps['dev_dependencies']:    
            if scanNPMJS:
                license = npmjs_get_license(dep)
                print(f"NPMJS - {dep} is license: {license}")

            if scanMavenRepository:
                license = mvnrepository_get_license(dep)
                print(f"Maven - {dep} license: {license}")

            # wait 0.5 seconds before checking the next dependency
            time.sleep(throttle)