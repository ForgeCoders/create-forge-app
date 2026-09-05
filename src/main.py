#!/usr/bin/env python3

from templates import list_templates
from generator import create_project

def main():
  print("🚀 Welcome to Create Forge App")
  print("\nAvailable templates:")

  for template in list_templates():
    print(f"- {template}")

if __name__ == "__main__":
  main()
