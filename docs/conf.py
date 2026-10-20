"""Configuration file for the Sphinx documentation builder."""
import os
import shutil
import re

shutil.copy2("../RELEASE.md", "./about/release-notes.md")

html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "rocm.docs.amd.com")
#html_context = {}
html_context = {
    "docs_header_version": "26.10"
}
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True
project = "AMD Simulation"

version = "26.10"
release = version
html_title = "AMD Simulation 26.10 documentation"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2026 Advanced Micro Devices, Inc. All rights reserved."
setting_all_article_info = True
all_article_info_os = ["linux"]
all_article_info_author = ""

#left_nav_title = f"AMD Simulation {version} documentation"

# Required settings
html_theme = "rocm_docs_theme"
html_theme_options = {
    "flavor": "rocm-simulation",
    "repository_url": "https://github.com/AMD-Ecosystem/simulation",
    "repository_branch": "docs/26.10",
    "path_to_docs": "docs",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_source_button": True,
    "use_download_button": True,
}
html_static_path = ["sphinx/static/css"]
html_css_files = ["rocm_custom.css"]
# Publish the llms.txt index at the docs site root and let
# rocm-docs-core generate llms-full.txt after each build (the llms.txt standard,
# https://llmstxt.org/). See the rocm-docs-core guide:
# https://rocm.docs.amd.com/projects/rocm-docs-core/en/latest/user_guide/llms.html
rocm_docs_generate_llms = True

extensions = ["rocm_docs"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

exclude_patterns = ['.venv']
