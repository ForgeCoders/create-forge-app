#!/usr/bin/env python3

from templates import list_templates, select_template
from generator import create_project

def main():
  print("🚀 Welcome to Create Forge App")

  chosen_templates = select_template()
  print(f"\nYou selected: {chosen_templates}")

if __name__ == "__main__":
  main()