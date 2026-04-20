#!/usr/bin/env python3
"""
Creates a Python Course setup email draft in Microsoft Outlook.

The email contains step-by-step installation instructions with Outlook-compatible
HTML (table-based layout, fully inline styles, PNG images) for:
  1. Python 3  (with "Add to PATH" highlighted)
  2. Visual Studio Code  (with "Add to PATH" highlighted)
  3. Python extension for VS Code  (by Microsoft)
  4. Git for Windows  (optional, with PATH option highlighted)
  5. VS Code built-in Git support  (optional, no extra extension required)

Requirements:
    pip install pywin32      # open Outlook draft (Windows only)

Bundled assets:
  email_assets/*.png     # checked-in PNG screenshots for Outlook

Usage:
    python create_setup_email.py
    Then fill in the recipients in the Outlook window that opens.
"""

import base64
from pathlib import Path


# ── helpers ────────────────────────────────────────────────────────────────────

def _make_img_src(svg: str) -> str:
    """Load a checked-in PNG asset and return it as a data URI.

    The script ships with PNG screenshots in email_assets/ so Outlook gets
    images it can render reliably without any external conversion libraries.
    """
    asset_path = Path(svg)
    if not asset_path.is_file():
        raise FileNotFoundError(f"Missing image asset: {asset_path}")
    return "data:image/png;base64," + base64.b64encode(asset_path.read_bytes()).decode()


# ── SVG: Python installer first screen ─────────────────────────────────────────

PYTHON_INSTALLER_SVG = """\
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="360"
     font-family="Segoe UI, Arial, sans-serif">
  <!-- window background -->
  <rect width="600" height="360" rx="8" fill="#f0f0f0" stroke="#bbb" stroke-width="1"/>
  <!-- title bar -->
  <rect width="600" height="36" rx="8" fill="#306998"/>
  <rect y="28" width="600" height="8" fill="#306998"/>
  <text x="16" y="23" fill="white" font-size="13" font-weight="bold">
    Install Python 3.13.0 (64-bit)
  </text>
  <circle cx="567" cy="18" r="7" fill="#ff5f57"/>
  <circle cx="549" cy="18" r="7" fill="#febc2e"/>
  <circle cx="531" cy="18" r="7" fill="#28c840"/>

  <!-- Python logo (simplified snake) -->
  <g transform="translate(30,58)">
    <path d="M28,0 Q0,0 0,28 L0,52 Q0,65 14,65 L42,65 Q52,65 52,55
             L52,50 L18,50 L18,40 L52,40 L52,28 Q52,0 24,0 Z" fill="#306998"/>
    <circle cx="36" cy="12" r="5" fill="white"/>
    <path d="M24,65 Q52,65 52,93 L52,117 Q52,130 38,130
             L10,130 Q0,130 0,120 L0,115 L34,115 L34,105 L0,105
             L0,93 Q0,65 28,65 Z" fill="#FFD43B"/>
    <circle cx="16" cy="118" r="5" fill="white"/>
  </g>

  <text x="200" y="88"  fill="#222" font-size="18" font-weight="bold">Python 3.13.0</text>
  <text x="200" y="110" fill="#555" font-size="12">The official Python 3 installer for Windows</text>

  <!-- divider -->
  <line x1="18" y1="210" x2="582" y2="210" stroke="#ccc" stroke-width="1"/>

  <!-- checkbox 1 – unchecked -->
  <rect  x="22" y="222" width="14" height="14" rx="2" fill="white" stroke="#aaa" stroke-width="1"/>
  <text  x="42" y="233" fill="#666" font-size="11">Use admin privileges when installing py.exe</text>

  <!-- checkbox 2 – CHECKED and highlighted row -->
  <rect  x="18" y="244" width="568" height="28" rx="4"
         fill="#fff8e1" stroke="#FFD43B" stroke-width="1.5"/>
  <rect  x="22" y="248" width="14" height="14" rx="2" fill="#306998" stroke="#306998"/>
  <text  x="27" y="259" fill="white" font-size="11" font-weight="bold">&#10003;</text>
  <text  x="42" y="260" fill="#000" font-size="12" font-weight="bold">
    Add python.exe to PATH
  </text>

  <!-- callout bubble -->
  <rect  x="340" y="249" width="210" height="24" rx="5"
         fill="#FFD43B" stroke="#c8a000" stroke-width="1.5"/>
  <text  x="350" y="265" fill="#333" font-size="11" font-weight="bold">
    &#9888;  Make sure this is checked!
  </text>
  <!-- callout arrow -->
  <defs>
    <marker id="a1" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0,8 3,0 6" fill="#c8a000"/>
    </marker>
  </defs>
  <line x1="339" y1="261" x2="305" y2="261"
        stroke="#c8a000" stroke-width="2" marker-end="url(#a1)"/>

  <!-- buttons -->
  <rect  x="22"  y="300" width="160" height="32" rx="5" fill="#306998"/>
  <text  x="102" y="320" fill="white" font-size="12" text-anchor="middle">Install Now</text>
  <rect  x="200" y="300" width="190" height="32" rx="5"
         fill="white" stroke="#306998" stroke-width="1.5"/>
  <text  x="295" y="320" fill="#306998" font-size="12" text-anchor="middle">
    Customize installation
  </text>
</svg>
"""


# ── SVG: VS Code installer "Select Additional Tasks" screen ────────────────────

VSCODE_INSTALLER_SVG = """\
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400"
     font-family="Segoe UI, Arial, sans-serif">
  <rect width="600" height="400" rx="8" fill="#f0f0f0" stroke="#bbb" stroke-width="1"/>
  <!-- title bar -->
  <rect width="600" height="36" rx="8" fill="#0078d4"/>
  <rect y="28" width="600" height="8" fill="#0078d4"/>
  <text x="16" y="23" fill="white" font-size="13" font-weight="bold">
    Setup - Visual Studio Code
  </text>
  <circle cx="567" cy="18" r="7" fill="#ff5f57"/>
  <circle cx="549" cy="18" r="7" fill="#febc2e"/>
  <circle cx="531" cy="18" r="7" fill="#28c840"/>

  <!-- header strip -->
  <rect x="18" y="50" width="564" height="54" rx="4" fill="#e8f4fd"/>
  <rect x="24" y="56" width="38" height="38" rx="6" fill="#0078d4"/>
  <text x="43"  y="81" fill="white" font-size="24" text-anchor="middle" font-weight="bold">&lt;/&gt;</text>
  <text x="72"  y="74" fill="#333" font-size="14" font-weight="bold">Select Additional Tasks</text>
  <text x="72"  y="90" fill="#666" font-size="11">
    Which additional tasks should be performed during installation?
  </text>

  <!-- checkbox rows -->
  <!-- row 1 -->
  <rect  x="28" y="118" width="14" height="14" rx="2" fill="white" stroke="#aaa" stroke-width="1"/>
  <text  x="48" y="129" fill="#555" font-size="11">Create a desktop icon</text>

  <!-- row 2 -->
  <rect  x="28" y="142" width="14" height="14" rx="2" fill="#0078d4" stroke="#0078d4"/>
  <text  x="33" y="153" fill="white" font-size="11">&#10003;</text>
  <text  x="48" y="153" fill="#444" font-size="11">
    Add "Open with Code" action to Windows Explorer file context menu
  </text>

  <!-- row 3 -->
  <rect  x="28" y="166" width="14" height="14" rx="2" fill="#0078d4" stroke="#0078d4"/>
  <text  x="33" y="177" fill="white" font-size="11">&#10003;</text>
  <text  x="48" y="177" fill="#444" font-size="11">
    Add "Open with Code" action to Windows Explorer directory context menu
  </text>

  <!-- row 4 -->
  <rect  x="28" y="190" width="14" height="14" rx="2" fill="#0078d4" stroke="#0078d4"/>
  <text  x="33" y="201" fill="white" font-size="11">&#10003;</text>
  <text  x="48" y="201" fill="#444" font-size="11">
    Register Code as an editor for supported file types
  </text>

  <!-- row 5 – ADD TO PATH (highlighted) -->
  <rect  x="18" y="214" width="568" height="28" rx="4"
         fill="#fff8e1" stroke="#FFD43B" stroke-width="1.5"/>
  <rect  x="28" y="218" width="14" height="14" rx="2" fill="#0078d4" stroke="#0078d4"/>
  <text  x="33" y="229" fill="white" font-size="11">&#10003;</text>
  <text  x="48" y="230" fill="#000" font-size="12" font-weight="bold">
    Add to PATH (available after restart)
  </text>

  <!-- callout -->
  <rect  x="370" y="216" width="200" height="24" rx="5"
         fill="#FFD43B" stroke="#c8a000" stroke-width="1.5"/>
  <text  x="380" y="232" fill="#333" font-size="11" font-weight="bold">
    &#9888;  Keep this checked!
  </text>
  <defs>
    <marker id="a2" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0,8 3,0 6" fill="#c8a000"/>
    </marker>
  </defs>
  <line x1="369" y1="228" x2="338" y2="228"
        stroke="#c8a000" stroke-width="2" marker-end="url(#a2)"/>

  <text x="22" y="262" fill="#888" font-size="10" font-style="italic">
    Note: A restart may be needed for PATH changes to take effect.
  </text>

  <!-- nav buttons -->
  <rect  x="396" y="352" width="90" height="30" rx="4" fill="#ddd" stroke="#bbb" stroke-width="1"/>
  <text  x="441" y="371" fill="#444" font-size="12" text-anchor="middle">Back</text>
  <rect  x="496" y="352" width="90" height="30" rx="4" fill="#0078d4"/>
  <text  x="541" y="371" fill="white" font-size="12" text-anchor="middle">Install</text>
</svg>
"""


# ── SVG: VS Code Extensions panel – Python extension ──────────────────────────

VSCODE_EXTENSIONS_SVG = """\
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="360"
     font-family="Segoe UI, Arial, sans-serif">
  <!-- VS Code window -->
  <rect width="600" height="360" rx="8" fill="#1e1e1e" stroke="#444" stroke-width="1"/>
  <!-- title bar -->
  <rect width="600" height="30" rx="8" fill="#323233"/>
  <rect y="22" width="600" height="8" fill="#323233"/>
  <text x="300" y="19" fill="#ccc" font-size="11" text-anchor="middle">
    Extensions: Marketplace &#8211; Visual Studio Code
  </text>
  <circle cx="567" cy="15" r="6" fill="#ff5f57"/>
  <circle cx="551" cy="15" r="6" fill="#febc2e"/>
  <circle cx="535" cy="15" r="6" fill="#28c840"/>

  <!-- activity bar -->
  <rect x="0" y="30" width="48" height="330" fill="#333333"/>
  <!-- extensions icon (active) -->
  <rect x="8" y="148" width="32" height="32" rx="4" fill="#0078d4"/>
  <text x="24" y="169" fill="white" font-size="18" text-anchor="middle">&#10753;</text>

  <!-- sidebar -->
  <rect x="48" y="30" width="236" height="330" fill="#252526"/>
  <!-- search box -->
  <rect x="55" y="38" width="222" height="24" rx="3"
        fill="#3c3c3c" stroke="#555" stroke-width="1"/>
  <text x="68" y="54" fill="#ccc" font-size="11">Python</text>

  <!-- Python extension row – highlighted / selected -->
  <rect x="48"  y="68" width="236" height="82" fill="#094771"/>
  <rect x="56"  y="76" width="44"  height="44" rx="6" fill="#306998"/>
  <text x="78"  y="105" fill="#FFD43B" font-size="24" font-weight="bold"
        text-anchor="middle">Py</text>
  <text x="108" y="94"  fill="white"   font-size="12" font-weight="bold">Python</text>
  <text x="108" y="108" fill="#9cdcfe" font-size="10">Microsoft</text>
  <text x="108" y="121" fill="#aaa"    font-size="10">&#9733; 4.8 &#183; 120M+ downloads</text>
  <text x="108" y="134" fill="#4ec9b0" font-size="10">IntelliSense, debug, lint&#8230;</text>

  <!-- second result (dimmed) -->
  <rect x="56"  y="158" width="44" height="44" rx="6" fill="#2d2d2d" stroke="#555" stroke-width="1"/>
  <text x="78"  y="186" fill="#aaa" font-size="18" text-anchor="middle">Py</text>
  <text x="108" y="173" fill="#ccc" font-size="11">Pylance</text>
  <text x="108" y="187" fill="#888" font-size="10">Microsoft</text>

  <!-- detail pane -->
  <rect x="284" y="30" width="316" height="330" fill="#1e1e1e"/>

  <!-- extension icon + meta -->
  <rect x="292" y="44" width="60" height="60" rx="8" fill="#306998"/>
  <text x="322" y="82" fill="#FFD43B" font-size="30" font-weight="bold"
        text-anchor="middle">Py</text>
  <text x="362" y="66"  fill="white"   font-size="15" font-weight="bold">Python</text>
  <text x="362" y="82"  fill="#9cdcfe" font-size="11">Microsoft</text>
  <text x="362" y="96"  fill="#888"    font-size="10">
    &#9733; 4.8 &#183; 120,000,000+ installs
  </text>

  <!-- Install button + callout -->
  <rect x="292" y="115" width="100" height="28" rx="4" fill="#0078d4"/>
  <text x="342" y="133" fill="white" font-size="12" text-anchor="middle"
        font-weight="bold">Install</text>

  <rect x="410" y="109" width="170" height="28" rx="5"
        fill="#FFD43B" stroke="#c8a000" stroke-width="1.5"/>
  <text x="495" y="127" fill="#333" font-size="11" font-weight="bold"
        text-anchor="middle">Click Install here</text>
  <defs>
    <marker id="a3" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0,8 3,0 6" fill="#c8a000"/>
    </marker>
  </defs>
  <line x1="409" y1="123" x2="395" y2="129"
        stroke="#c8a000" stroke-width="2" marker-end="url(#a3)"/>

  <text x="292" y="168" fill="#ccc" font-size="10">IntelliSense, Linting, Debugging,</text>
  <text x="292" y="183" fill="#ccc" font-size="10">Jupyter notebook support,</text>
  <text x="292" y="198" fill="#ccc" font-size="10">variable explorer, test explorer, and more!</text>
</svg>
"""


# ── SVG: Git installer PATH environment screen ─────────────────────────────────

GIT_INSTALLER_SVG = """\
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="390"
     font-family="Segoe UI, Arial, sans-serif">
  <rect width="600" height="390" rx="8" fill="#f0f0f0" stroke="#bbb" stroke-width="1"/>
  <!-- title bar -->
  <rect width="600" height="36" rx="8" fill="#f05032"/>
  <rect y="28" width="600" height="8" fill="#f05032"/>
  <text x="16" y="23" fill="white" font-size="13" font-weight="bold">
    Git 2.x Setup &#8211; Adjusting your PATH environment
  </text>
  <circle cx="567" cy="18" r="7" fill="#ff5f57"/>
  <circle cx="549" cy="18" r="7" fill="#febc2e"/>
  <circle cx="531" cy="18" r="7" fill="#28c840"/>

  <!-- Git logo -->
  <rect x="22" y="50" width="44" height="44" rx="6" fill="#f05032"/>
  <text x="44" y="81" fill="white" font-size="28" font-weight="bold"
        text-anchor="middle">&#9095;</text>

  <text x="80" y="72" fill="#333" font-size="14" font-weight="bold">
    Adjusting your PATH environment
  </text>
  <text x="80" y="90" fill="#666" font-size="11">
    How would you like to use Git from the command line and other software?
  </text>

  <!-- Option 1 – not selected -->
  <circle cx="30" cy="125" r="7" fill="white" stroke="#aaa" stroke-width="1.5"/>
  <text x="44"  y="130" fill="#555" font-size="11" font-weight="bold">Use Git from Git Bash only</text>
  <text x="44"  y="145" fill="#888" font-size="10">
    Git will not modify PATH. Use Git Bash terminal only.
  </text>

  <!-- Option 2 – RECOMMENDED / SELECTED -->
  <rect x="18" y="160" width="568" height="82" rx="5"
        fill="#e8f4fd" stroke="#0078d4" stroke-width="2"/>
  <circle cx="30" cy="178" r="7" fill="#0078d4" stroke="#0078d4" stroke-width="1.5"/>
  <circle cx="30" cy="178" r="3" fill="white"/>
  <text x="44" y="183" fill="#000" font-size="12" font-weight="bold">
    Git from the command line and also from 3rd-party software
  </text>
  <rect  x="44" y="190" width="96" height="15" rx="3" fill="#0078d4"/>
  <text  x="92" y="201" fill="white" font-size="9" text-anchor="middle"
         font-weight="bold">Recommended</text>
  <text  x="44" y="218" fill="#555" font-size="10">
    Adds minimal Git wrappers to your PATH so you can use Git from
  </text>
  <text  x="44" y="232" fill="#555" font-size="10">
    PowerShell, Command Prompt and Visual Studio Code.
  </text>

  <!-- callout -->
  <rect  x="372" y="162" width="200" height="24" rx="5"
         fill="#FFD43B" stroke="#c8a000" stroke-width="1.5"/>
  <text  x="382" y="178" fill="#333" font-size="11" font-weight="bold">
    &#10003; Select this option!
  </text>
  <defs>
    <marker id="a4" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0,8 3,0 6" fill="#c8a000"/>
    </marker>
  </defs>
  <line x1="371" y1="174" x2="354" y2="183"
        stroke="#c8a000" stroke-width="2" marker-end="url(#a4)"/>

  <!-- Option 3 – not selected -->
  <circle cx="30" cy="262" r="7" fill="white" stroke="#aaa" stroke-width="1.5"/>
  <text x="44"  y="267" fill="#555" font-size="11" font-weight="bold">
    Use Git and optional Unix tools from Command Prompt
  </text>
  <text x="44"  y="282" fill="#888" font-size="10">
    Overrides built-in Windows tools (find, sort&#8230;). Not recommended.
  </text>

  <!-- nav buttons -->
  <rect  x="402" y="342" width="90" height="30" rx="4" fill="#ddd" stroke="#bbb" stroke-width="1"/>
  <text  x="447" y="361" fill="#444" font-size="12" text-anchor="middle">Back</text>
  <rect  x="502" y="342" width="90" height="30" rx="4" fill="#0078d4"/>
  <text  x="547" y="361" fill="white" font-size="12" text-anchor="middle">Next</text>
</svg>
"""


# ── HTML email body ─────────────────────────────────────────────────────────────

def _build_html(img_py: str, img_vsc: str, img_ext: str, img_git: str) -> str:
    """Return Outlook-compatible HTML for the email body.

    Uses table-based layout with fully inlined styles — no CSS <style> block,
    no gradients, no border-radius, no box-shadow (all ignored by Outlook).
    Images must be PNG data URIs; SVG is silently dropped by Outlook.
    """
    F = "font-family:Calibri,'Segoe UI',Arial,sans-serif"
    PAGE_BG = "#eef2f7"
    PANEL_BG = "#ffffff"
    TEXT = "#1f2937"
    MUTED = "#6b7280"
    BRAND = "#1f4e79"
    BRAND_LINE = "#4d7aa2"
    BRAND_SOFT = "#f4f8fb"
    WARN_BORDER = "#c69214"
    WARN_BG = "#fff7df"
    SUCCESS_BORDER = "#2f6f44"
    SUCCESS_BG = "#eef7f1"
    INFO_BORDER = "#245f8f"
    INFO_BG = "#edf5fb"
    CODE_BG = "#1f2937"
    CODE_TEXT = "#b8f2e6"
    DIVIDER = "#d8e0e8"
    DARK_TEXT = "color:#ffffff;mso-style-textfill-type:solid;mso-style-textfill-fill-color:#ffffff;"
    BASE = f"{F};font-size:11pt;color:{TEXT}"

    # ── inline component helpers ────────────────────────────────────────────

    def _p(html):
        return f'<p style="{BASE};margin:8px 0;">{html}</p>\n'

    def _li(html):
        return f'<li style="{BASE};margin:5px 0;line-height:1.6;">{html}</li>\n'

    def _h2(html):
        return (
            f'<table width="100%" cellpadding="0" cellspacing="0" border="0"'
            f' style="margin:32px 0 8px 0;border-collapse:collapse;">\n'
            f'<tr>\n'
        f'  <td width="5" bgcolor="{BRAND}"'
        f' style="background-color:{BRAND};width:5px;">&nbsp;</td>\n'
            f'  <td style="padding:8px 10px;{F};font-size:14pt;'
        f'color:{BRAND};font-weight:bold;">{html}</td>\n'
            f'</tr>\n</table>\n'
        )

    def _h3(text):
      return f'<p style="{F};font-size:12pt;color:{TEXT};font-weight:bold;margin:16px 0 8px 0;">{text}</p>\n'

    def _code(text):
        return (
            '<!--[if mso]>'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" '
            f'style="display:inline-table;vertical-align:middle;border-collapse:separate;">'
            f'<tr><td bgcolor="{CODE_BG}" '
            f'style="background-color:{CODE_BG};color:{CODE_TEXT};padding:2px 6px;'
            f'font-family:Consolas,\'Courier New\',monospace;font-size:10pt;white-space:nowrap;">'
            f'{text}</td></tr></table><![endif]-->'
            '<!--[if !mso]><!-->'
            f'<span style="font-family:Consolas,\'Courier New\',monospace;'
            f'font-size:10pt;background-color:{CODE_BG};color:{CODE_TEXT};white-space:nowrap;">'
            f'&nbsp;{text}&nbsp;</span>'
            '<!--<![endif]-->'
        )

    def _kbd(text):
        return (
            '<!--[if mso]>'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" '
            f'style="display:inline-table;vertical-align:middle;border-collapse:separate;">'
            f'<tr><td bgcolor="#e5e7eb" '
            f'style="background-color:#e5e7eb;border:1px solid #c7d0da;color:{TEXT};'
            f'padding:1px 5px;font-size:10pt;white-space:nowrap;{F};">'
            f'{text}</td></tr></table><![endif]-->'
            '<!--[if !mso]><!-->'
            f'<span style="background-color:#e5e7eb;border:1px solid #c7d0da;color:{TEXT};'
            f'font-size:10pt;white-space:nowrap;{F};">&nbsp;{text}&nbsp;</span>'
            '<!--<![endif]-->'
        )

    def _badge(text):
        return (
            '<!--[if mso]>'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" '
            f'style="display:inline-table;vertical-align:middle;border-collapse:separate;">'
            f'<tr><td bgcolor="{SUCCESS_BORDER}" '
            f'style="background-color:{SUCCESS_BORDER};padding:1px 8px;{DARK_TEXT}'
            f'font-size:9pt;font-weight:bold;white-space:nowrap;">{text}</td></tr></table><![endif]-->'
            '<!--[if !mso]><!-->'
            f'<span style="background-color:{SUCCESS_BORDER};{DARK_TEXT}'
            f'font-size:9pt;font-weight:bold;white-space:nowrap;">&nbsp;{text}&nbsp;</span>'
            '<!--<![endif]-->'
        )

    def _num(n):
        return (
            '<!--[if mso]>'
            f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" '
            f'style="display:inline-table;vertical-align:middle;border-collapse:separate;">'
            f'<tr><td bgcolor="{BRAND}" '
            f'style="background-color:{BRAND};padding:2px 9px;{DARK_TEXT}'
            f'font-weight:bold;font-size:13pt;white-space:nowrap;">{n}</td>'
            f'<td style="width:8px;font-size:8px;line-height:8px;">&nbsp;</td></tr></table><![endif]-->'
            '<!--[if !mso]><!-->'
            f'<span style="background-color:{BRAND};{DARK_TEXT}'
            f'font-weight:bold;font-size:13pt;white-space:nowrap;">&nbsp;{n}&nbsp;</span>&nbsp;'
            '<!--<![endif]-->'
        )

    def _box(content, border_color, bg_color, margin="14px 0"):
        return (
            f'<table width="100%" cellpadding="0" cellspacing="0" border="0"'
            f' style="margin:{margin};border-collapse:collapse;">\n'
            f'<tr>\n'
            f'  <td width="5" bgcolor="{border_color}"'
            f' style="background-color:{border_color};width:5px;">&nbsp;</td>\n'
            f'  <td bgcolor="{bg_color}"'
            f' style="background-color:{bg_color};padding:16px 18px;{BASE};">'
            f'{content}</td>\n'
            f'</tr>\n</table>\n'
        )

    def _step(c):  return _box(c, BRAND, BRAND_SOFT)
    def _warn(c):  return _box(c, WARN_BORDER, WARN_BG, "12px 0")
    def _opt(c):   return _box(c, SUCCESS_BORDER, SUCCESS_BG)
    def _ok(c):    return _box(c, INFO_BORDER, INFO_BG)

    def _cmd(*lines):
        body = "".join(ln + "<br>\n" for ln in lines)
        return (
            f'<table width="100%" cellpadding="0" cellspacing="0" border="0"'
            f' style="margin:10px 0;border-collapse:collapse;">\n'
            f'<tr>\n'
            f'  <td width="4" bgcolor="#58c4b4"'
            f' style="background-color:#58c4b4;width:4px;">&nbsp;</td>\n'
            f'  <td bgcolor="{CODE_BG}"'
            f' style="background-color:{CODE_BG};padding:14px 16px;'
            f'font-family:Consolas,\'Courier New\',monospace;font-size:10pt;'
            f'color:{CODE_TEXT};line-height:1.7;">{body}</td>\n'
            f'</tr>\n</table>\n'
        )

    def _dl(href, color, label):
        return (
        '<!--[if mso]>'
        f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" '
        f'style="border-collapse:separate;margin:6px 0;">'
        f'<tr><td bgcolor="{color}" '
        f'style="background-color:{color};padding:8px 20px;{DARK_TEXT}'
        f'font-weight:bold;{F};font-size:11pt;">'
        f'<a href="{href}" style="{DARK_TEXT}text-decoration:none;">{label}</a>'
        f'</td></tr></table><![endif]-->'
        '<!--[if !mso]><!-->'
        f'<a href="{href}" style="display:inline-block;background-color:{color};'
        f'{DARK_TEXT}text-decoration:none;padding:8px 20px;font-weight:bold;'
        f'{F};font-size:11pt;margin:6px 0;">{label}</a>'
        '<!--<![endif]-->'
        )

    def _img(src, alt, caption):
        if not src:
            return ""
        return (
            f'<table width="100%" cellpadding="0" cellspacing="0" border="0"'
            f' style="margin:20px 0;">\n'
            f'<tr><td align="center">\n'
            f'  <img src="{src}" alt="{alt}" width="590"'
            f' style="display:block;max-width:590px;width:100%;border:1px solid #dddddd;">\n'
            f'  <p style="{F};font-size:9pt;color:{MUTED};margin:6px 0 0 0;'
            f'font-style:italic;text-align:center;">{caption}</p>\n'
            f'</td></tr>\n</table>\n'
        )

    HR = (
        '<table width="100%" cellpadding="0" cellspacing="0" border="0"'
        ' style="margin:28px 0;">\n'
          f'<tr><td style="border-top:1px solid {DIVIDER};font-size:1px;line-height:1px;">'
        '&nbsp;</td></tr>\n</table>\n'
    )
    prompt = '<span style="color:#94a3b8;">C:\\&gt;&nbsp;</span>'

    # ── assemble ────────────────────────────────────────────────────────────

    return (
        '<!DOCTYPE html>\n'
        '<html>\n'
        '<head>\n'
        '<meta charset="UTF-8">\n'
        '<meta name="color-scheme" content="light dark">\n'
        '<meta name="supported-color-schemes" content="light dark">\n'
        '<!--[if mso]><xml><o:OfficeDocumentSettings><o:AllowPNG/>'
        '</o:OfficeDocumentSettings></xml><![endif]-->\n'
        '</head>\n'
        f'<body style="margin:0;padding:0;background-color:{PAGE_BG};">\n'
        '<table width="600" cellpadding="0" cellspacing="0" border="0" align="center"'
        ' style="width:600px;">\n'
        f'<tr><td style="padding:20px;background-color:{PANEL_BG};' + BASE + ';">\n\n'

        # ── intro banner ─────────────────────────────────────────────────────
        '<table width="100%" cellpadding="0" cellspacing="0" border="0"'
        ' style="border-collapse:collapse;">\n'
        '<tr>\n'
        f'  <td bgcolor="{BRAND}" style="background-color:{BRAND};padding:22px 26px;">\n'
        '    <h1 style="' + F + ';font-size:19pt;' + DARK_TEXT + 'margin:0 0 12px 0;'
        f'padding-bottom:10px;border-bottom:2px solid {BRAND_LINE};">\n'
        '      &#127822; Python Course &#8212; Setting Up Your Windows Development Environment\n'
        '    </h1>\n'
        '    <p style="' + F + ';font-size:11pt;' + DARK_TEXT + 'margin:5px 0;">'
        'Welcome! Please install all the tools listed below '
        '<strong>before our first session</strong>.</p>\n'
        '    <p style="' + F + ';font-size:11pt;' + DARK_TEXT + 'margin:5px 0;">'
        'The whole process takes around <strong>15&#8211;20 minutes</strong>. '
        'If you hit any problems, just reply to this email and we will help you.</p>\n'
        '  </td>\n'
        '</tr>\n'
        '</table>\n\n'
        '<table width="100%" cellpadding="0" cellspacing="0" border="0"'
        ' style="border-collapse:collapse;">\n'
        '<tr><td height="24" style="height:24px;font-size:24px;line-height:24px;">&nbsp;</td></tr>\n'
        '</table>\n\n'

        # ── tools overview ────────────────────────────────────────────────────
        + _h2('&#128203; Tools Overview')
        + '<ul style="padding-left:22px;margin:0 0 16px 0;">\n'
        + _li('<strong>Python 3</strong> &#8212; the language interpreter')
        + _li('<strong>Visual Studio Code</strong> &#8212; lightweight, powerful code editor (free)')
        + _li('<strong>Python extension for VS Code</strong> (by Microsoft) &#8212;'
              ' IntelliSense, debugging, linting, Jupyter support')
        + _li(f'<strong>Git for Windows</strong> {_badge("OPTIONAL")} &#8212; version control')
          + _li(f'<strong>VS Code built-in Git support</strong> {_badge("OPTIONAL")}'
            f' &#8212; source control directly inside the editor once Git is installed')
        + '</ul>\n\n'
        + HR

        # ── step 1: python ────────────────────────────────────────────────────
        + _h2(f'{_num(1)} Install Python')
        + _step(
            _p('Download the latest stable Python&nbsp;3 from the official website:')
            + _dl('https://www.python.org/downloads/', '#306998',
              '&#11015;&nbsp;python.org/downloads')
            + _p('Click the large yellow <em>&#8220;Download Python 3.x.x&#8221;</em>'
                 ' button &#8212; the site detects your OS automatically and offers'
                 ' the correct 64-bit Windows installer.')
          )
        + _h3('Installation steps')
        + '<ol style="padding-left:22px;margin:0 0 12px 0;">\n'
        + _li(f'Run the downloaded {_code(".exe")} file.')
        + _li('<strong>Before doing anything else, tick &#8220;Add python.exe to'
              ' PATH&#8221;</strong> at the bottom of the first screen (see image below).')
        + _li('Click <strong>Install Now</strong> and wait for it to finish.')
        + _li('Click <strong>Close</strong>.')
        + '</ol>\n'
        + _warn(
            '<strong>&#9888;&nbsp;Critical &#8212; Add Python to PATH:</strong><br>'
            'The <em>&#8220;Add python.exe to PATH&#8221;</em> checkbox is'
            ' <strong>unchecked by default</strong> in some versions of the installer.'
            ' Without it, Python will not be usable from the terminal, Command Prompt,'
            ' or VS Code. Do not skip it!'
          )
        + _img(img_py,
               'Python 3 installer showing the Add python.exe to PATH checkbox highlighted',
               'Python 3 installer &#8212; check &#8220;Add python.exe to PATH&#8221;'
               ' before clicking Install Now')
        + _h3('Verify the installation')
        + _p(f'Open <strong>Command Prompt</strong>'
             f' ({_kbd("Win")}+{_kbd("R")} &#8594; type {_code("cmd")}'
             f' &#8594; {_kbd("Enter")}) and run:')
        + _cmd(f'{prompt}python --version', 'Python 3.13.x', '',
               f'{prompt}pip --version', 'pip 24.x from ...')
        + _p('Seeing version numbers means Python is installed correctly. &#9989;')
        + HR

        # ── step 2: vs code ───────────────────────────────────────────────────
        + _h2(f'{_num(2)} Install Visual Studio Code')
        + _step(
            _p('VS Code is a free, open-source code editor built by Microsoft.'
               ' It runs on Windows, macOS, and Linux.')
            + _dl('https://code.visualstudio.com/', '#0078d4',
              '&#11015;&nbsp;code.visualstudio.com')
            + _p('Click <strong>Download for Windows</strong>.'
                 ' Choose the <em>System Installer</em> (recommended over the User Installer).')
          )
        + _h3('Installation steps')
        + '<ol style="padding-left:22px;margin:0 0 12px 0;">\n'
        + _li(f'Run the downloaded {_code("VSCodeSetup-x64-*.exe")} file.')
        + _li('Accept the licence agreement and click <strong>Next</strong>.')
        + _li('Leave the destination folder as default and click <strong>Next</strong>.')
        + _li('On the <strong>&#8220;Select Additional Tasks&#8221;</strong> screen,'
              ' make sure all checkboxes are ticked &#8212; especially:<br>'
              '&#9989;&nbsp;Add &#8220;Open with Code&#8221; to Windows Explorer context menu<br>'
              '&#9989;&nbsp;<strong>Add to PATH (available after restart)</strong>')
        + _li('Click <strong>Install</strong>, wait for it to finish, then click <strong>Finish</strong>.')
        + '</ol>\n'
        + _warn(
            f'<strong>&#9888;&nbsp;Add VS Code to PATH:</strong><br>'
            f'Checking <strong>&#8220;Add to PATH&#8221;</strong> on the Additional Tasks'
            f' screen lets you open any folder in VS Code from any terminal window simply'
            f' by typing {_code("code .")}. Very useful &#8212; keep this ticked!'
          )
        + _img(img_vsc,
               'VS Code installer Select Additional Tasks screen with Add to PATH highlighted',
               'VS Code installer &#8212; ensure &#8220;Add to PATH&#8221; is checked'
               ' on the Additional Tasks screen')
        + HR

        # ── step 3: python extension ──────────────────────────────────────────
        + _h2(f'{_num(3)} Install the Python Extension for VS Code')
        + _step(
            _p('This official Microsoft extension adds Python IntelliSense (auto-complete),'
               ' linting, debugging, Jupyter notebook support, variable explorer,'
               ' and much more to VS Code.')
          )
        + _h3('Installation steps')
        + '<ol style="padding-left:22px;margin:0 0 12px 0;">\n'
        + _li('Open <strong>Visual Studio Code</strong>.')
        + _li(f'Press {_kbd("Ctrl")}+{_kbd("Shift")}+{_kbd("X")} to open the'
              f' <strong>Extensions</strong> panel (or click the grid icon in the left sidebar).')
        + _li(f'Type {_code("Python")} in the search box.')
        + _li('Click on <strong>&#8220;Python&#8221;</strong> by <strong>Microsoft</strong>'
              ' &#8212; it will be the top result with 100&#8239;M+ installs.')
        + _li('Click the <strong>Install</strong> button.')
        + '</ol>\n'
        + _img(img_ext,
               'VS Code Extensions panel showing Python extension by Microsoft',
               'Extensions panel &#8212; search for &#8220;Python&#8221; and install'
               ' the one published by Microsoft')
          + _p(f'Extension ID: {_code("ms-python.python")}')
          + _dl('https://marketplace.visualstudio.com/items?itemName=ms-python.python',
            INFO_BORDER, 'View in VS Code Marketplace')
        + HR

        # ── step 4: git ───────────────────────────────────────────────────────
        + _h2(f'{_num(4)} Install Git for Windows {_badge("OPTIONAL")}')
        + _opt(
            _p('Git is the world&#8217;s most widely used version control system.'
               ' It&#8217;s not strictly required for the Python course itself, but it is'
               ' an essential tool for any developer and we recommend installing it now.')
            + _dl('https://git-scm.com/download/win', '#f05032',
              '&#11015;&nbsp;git-scm.com/download/win')
            + _p('The download starts automatically when you visit the page'
                 ' (it detects 64-bit Windows).')
          )
        + _h3('Installation steps')
        + '<ol style="padding-left:22px;margin:0 0 12px 0;">\n'
        + _li('Run the downloaded installer.')
        + _li('Click <strong>Next</strong> through the first several screens &#8212;'
              ' the defaults are all fine.')
        + _li('On the <strong>&#8220;Adjusting your PATH environment&#8221;</strong>'
              ' screen, select the <strong>recommended</strong> option:<br>'
              '<strong>&#8220;Git from the command line and also from 3rd-party'
              ' software&#8221;</strong>')
        + _li('Continue clicking <strong>Next</strong> through the remaining screens'
              ' (defaults are fine), then click <strong>Install</strong>.')
        + '</ol>\n'
        + _warn(
            '<strong>&#9888;&nbsp;Add Git to PATH:</strong><br>'
            'Choose the <em>recommended</em> option on the PATH screen.'
            ' This ensures Git works seamlessly inside VS Code&#8217;s built-in terminal,'
            ' PowerShell, and Command Prompt &#8212; with zero extra configuration.'
          )
        + _img(img_git,
               'Git installer PATH environment screen with the recommended option highlighted',
               'Git installer &#8212; select the recommended option to add Git to your PATH')
        + _h3('Verify the installation')
        + _cmd(f'{prompt}git --version', 'git version 2.x.x.windows.x')
        + HR

          # ── step 5: built-in git support ─────────────────────────────────────
          + _h2(f'{_num(5)} Use Git in VS Code {_badge("OPTIONAL")}')
        + _opt(
          _p('VS Code already includes built-in Git support, so you do not need'
             ' to install an extra Git extension for the course.')
            + '<ol style="padding-left:22px;margin:4px 0 8px 0;">\n'
          + _li('Make sure <strong>Git for Windows</strong> is installed first if you want'
            ' to use version control inside VS Code.')
          + _li('Open <strong>Visual Studio Code</strong> and click the'
            ' <strong>Source Control</strong> icon in the left sidebar,'
            ' or press ' + _kbd("Ctrl") + '+' + _kbd("Shift") + '+' + _kbd("G") + '.')
          + _li('Open a folder that contains a Git repository, or choose'
            ' <strong>Initialize Repository</strong> to start a new one.')
          + _li('Use the Source Control view to review changed files, write commit'
            ' messages, and commit your work without leaving the editor.')
            + '</ol>\n'
          + _warn('No additional Git extension is required for this course.'
              ' Installing <strong>Git for Windows</strong> is enough to enable'
              ' VS Code&#8217;s built-in Source Control features.')
          )
        + HR

        # ── final verification ─────────────────────────────────────────────────
        + _h2('&#9989; Final Verification')
        + _ok(
            _p('Once everything is installed, open <strong>Command Prompt</strong> or'
             ' <strong>PowerShell</strong> and run the commands below to confirm'
             ' the tools are on your PATH. The Git check is optional if you skipped Git for Windows:')
          )
        + _cmd(
            f'{prompt}python --version', 'Python 3.13.x', '',
            f'{prompt}pip --version', 'pip 24.x from ...', '',
            f'{prompt}code --version', '1.9x.x', '...', '',
            f'{prompt}git --version', 'git version 2.x.x.windows.x',
          )
        + _p('All four commands returning version numbers means your development'
             ' environment is ready to go. &#127881;')
        + _p('If a command says <em>&#8220;is not recognized as an internal or external'
             ' command&#8221;</em>, the tool was not added to PATH correctly. Try'
             ' re-running its installer and ticking the PATH option &#8212; or reply'
             ' to this email and we will help you sort it out.')

        # ── footer ─────────────────────────────────────────────────────────────
        + '<table width="100%" cellpadding="0" cellspacing="0" border="0"'
        '  style="margin-top:38px;border-top:2px solid #FFD43B;">\n'
        '<tr><td style="padding-top:18px;' + F + ';font-size:10pt;color:#888888;">\n'
        '  <p style="' + F + ';font-size:10pt;color:#888888;margin:5px 0;">'
        '<strong>Questions?</strong> Reply to this email and we will help you'
        ' get set up before the first session.</p>\n'
        '  <p style="' + F + ';font-size:10pt;color:#888888;margin:5px 0;">'
        'Looking forward to seeing you in class! &#127822;</p>\n'
        '  <br>\n'
        '  <p style="' + F + ';font-size:10pt;color:#888888;margin:5px 0;">'
        '<strong>Your Python Course Instructor</strong></p>\n'
        '</td></tr>\n</table>\n\n'

        '</td></tr>\n</table>\n'
        '</body>\n</html>\n'
    )


OUTPUT_FILE = "setup_email.html"
ASSET_DIR = Path(__file__).with_name("email_assets")


def main() -> None:
    """Build the email HTML body and save it to a file."""
    print("Loading bundled PNG assets …")
    img_py  = _make_img_src(ASSET_DIR / "python_installer.png")
    img_vsc = _make_img_src(ASSET_DIR / "vscode_installer.png")
    img_ext = _make_img_src(ASSET_DIR / "vscode_python_extension.png")
    img_git = _make_img_src(ASSET_DIR / "git_installer.png")

    print("Building HTML email body …")
    html = _build_html(img_py, img_vsc, img_ext, img_git)

    print(f"Saving to {OUTPUT_FILE} …")
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"Saved: {OUTPUT_FILE}")

    print("Opening Outlook draft …")
    try:
        import win32com.client
        outlook = win32com.client.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)   # 0 = olMailItem
        mail.Subject = (
            "Python Course \u2014 Setting Up Your Windows Development Environment"
        )
        mail.HTMLBody = html
        mail.Display(False)            # non-modal window
        print("\nDone! Add recipients in Outlook and click Send when ready.")
    except ImportError:
        print(
            "\npywin32 is not installed \u2014 could not open Outlook automatically.\n"
            f"Open {OUTPUT_FILE} in a browser to preview, then paste into an Outlook email.\n"
            "Install pywin32 with:  pip install pywin32"
        )


if __name__ == "__main__":
    main()
