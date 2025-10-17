#!/usr/bin/env python3
"""
Webease CLI Entry Point
"""

import sys
from src.webease.cli import main

if __name__ == '__main__':
    if len(sys.argv) > 1 and not sys.argv[1].startswith('-'):
        filename = sys.argv[1]
        save_flag = '--save' in sys.argv
        output_dir = 'output'
        
        if '--output' in sys.argv or '-o' in sys.argv:
            try:
                idx = sys.argv.index('--output') if '--output' in sys.argv else sys.argv.index('-o')
                output_dir = sys.argv[idx + 1]
            except (IndexError, ValueError):
                pass
        
        main([filename, '--save'] if save_flag else [filename], standalone_mode=False)
    else:
        from src.webease.cli import cli
        cli()
