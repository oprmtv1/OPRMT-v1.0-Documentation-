

SECURITY.md

Security Policy for the OPRMT™ Open Prompt Standard

Copyright © 2025 ImperialTurf LLC
All rights reserved.


---

1. Purpose

The OPRMT™ Standard is a foundational open framework used by developers, educators, and organizations worldwide.
To protect the integrity of the specification and its ecosystem, all contributors must follow this security policy when identifying or reporting vulnerabilities, misconfigurations, or malicious activity.

This document defines the official process for:

Reporting security issues

Preventing malicious contributions

Reviewing and resolving vulnerabilities

Communicating security updates to the community



---

2. Scope

This policy applies to:

The OPRMT™ Specification

Related documentation

Any official tools, scripts, or validators in this repository

The GitHub repo structure and versioning

OPRMT™ examples, templates, and reference implementations


It does not govern third-party tools or platforms built using OPRMT™.


---

3. What Qualifies as a Security Issue

Security issues include, but are not limited to:

3.1 Malicious or Harmful Contributions

Backdoors in example prompts or tools

Manipulation of the standard to introduce unsafe behaviors

Unauthorized modification attempts

PRs designed to break compatibility or introduce vulnerabilities


3.2 Content Integrity Risks

Prompts that encourage unsafe, harmful, or illegal behavior

Incorrect or misleading instructions that compromise user safety

Structural changes that weaken OPRMT™ principles


3.3 Repository Risks

Exposed secrets or API keys

Broken permissions or access settings

GitHub Actions vulnerabilities

Dependency issues in official tooling



---

4. Reporting a Security Issue

Security vulnerabilities must not be disclosed publicly.

To report a security issue, email:

support@oprmt.com

Include:

Detailed description of the issue

Steps to reproduce

Severity level (if known)

Any supporting evidence or logs

Your GitHub username (optional)

Whether you are a member of the OPRMT™ Community


We acknowledge all reports within 48 hours.


---

5. How We Handle Reports

5.1 Initial Triage

Maintainers confirm the issue, classify severity, and determine whether immediate action is required.

5.2 Internal Review

A Maintainer and an Oversight Reviewer evaluate impact and propose a fix.
Critical issues trigger fast-track review.

5.3 Patch Development

Fixes are developed in a private branch.
Changes are reviewed by at least two Maintainers before merging.

5.4 Disclosure

Once resolved, the security issue is:

Added to the SECURITY section of the next version’s CHANGELOG

Communicated privately to affected parties

Publicized only after a fix is released



---

6. Preventing Security Vulnerabilities

Community Contributors and Maintainers must follow these preventative rules:

6.1 Always Verify Structure

All contributions must follow OPRMT™ formatting:

Objective

Parameters

Results

Method

Tools


Improper formatting may hide malicious content.

6.2 Check for External Links

Links must be relevant, safe, and free of tracking or malicious redirects.

6.3 Validate Tools/Examples

Any tool or code snippet must be reviewed for:

Unsafe outputs

Harmful automation

Model jailbreak attempts

Dependencies with known vulnerabilities


6.4 Zero Trust for Arbitrary Changes

Suspicious PRs or issues may trigger:

Identity verification

Membership confirmation

Temporary contribution lockouts



---

7. Maintainer Responsibilities

Maintainers must:

Enforce this policy consistently

Reject contributions that pose security risks

Escalate concerns to ImperialTurf LLC

Protect the repository from spam, bots, or automated malicious PRs


ImperialTurf LLC retains full authority to remove Maintainers for non-compliance.


---

8. Community Member Requirements

Members of the OPRMT™ Community who contribute must maintain:

Proper conduct

Accurate submissions

Responsible disclosure practices

Awareness of safety guidelines


Membership may be suspended for violations.


---

9. Non-Compliance

Violating this policy may result in:

Immediate PR closure

Temporary or permanent ban from contributing

Suspension of OPRMT™ Community membership

Legal action for malicious or trademark-related abuse



---

10. Contact

For security questions or reports:
support@oprmt.com


