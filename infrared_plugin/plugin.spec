---
plugin_type: install
subparsers:
    collect-logs:
        description: Collect logs - TripleOQ deployment		#check_for_in_here
        include_groups: ["Ansible options", "Inventory", "Common options", "Answers file"]
        groups:
            - title: Collect Artcl
              options:
                  artcl-collect:
                      type: Bool
                      help: |
                          Collect artcl
                      default: true
                  
            - title: Publish artcl
              options:
                  artcl-publish:
                      type: Bool
                      help: |
                          Publish artcl
                      default: false
