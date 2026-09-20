---
name: jing-jing-clarifier
description: Revise technical or general text that is primarily Traditional Chinese by reducing unnecessary Chinese-English mixing and standardizing terminology, while preserving brands, proper nouns, APIs, code, commands, paths, versions, identifiers, numbers, and other exact literals. Use when the user asks for Chinese polishing, technical-document localization, Jing-Jing-style cleanup, terminology normalization, or removal of unnecessary English.
---

# JING JING Clarifier

## Goal

Revise text that is primarily Traditional Chinese but contains unnecessary English into natural, clear, and consistent Traditional Chinese.

Priority order:

1. Preserve the original facts, technical meaning, and logic.
2. Preserve every exact literal that cannot be safely rewritten.
3. Reduce unnecessary Chinese-English mixing.
4. Use natural Taiwan Traditional Chinese and terminology appropriate to the domain.
5. Keep terminology and writing style consistent throughout the document.

This Skill is not intended to eliminate all English. Preserve proper nouns, established industry terminology, and terms whose translation would reduce precision.

## When to use

Use this Skill for:

- Traditional Chinese copy editing.
- Localizing technical documentation into Traditional Chinese.
- Removing unnecessary English from otherwise Chinese sentences.
- Cleaning up awkward Chinese-English code-switching (sometimes called “Jing Jing style”).
- Standardizing Traditional Chinese technical terminology.
- Improving Chinese readability without changing engineering meaning.

Do not apply it mechanically when the user only asks to translate one word, explain a term, or explicitly wants to preserve the existing mixed-language style.

## Terminology decision order

When terminology choices conflict, use this order:

1. Vocabulary, formatting, and glossary terms explicitly specified by the user.
2. Terminology already established and used consistently in the current document or project.
3. Traditional Chinese terminology commonly used in the relevant professional field in Taiwan.
4. A natural Chinese translation that can be chosen confidently without semantic loss.
5. Keep the English term when translation may introduce ambiguity, distortion, or unnatural wording.

Never force a translation merely to reduce the amount of English.

## Protected literals

Unless the user explicitly asks to change them, treat the following as protected literals and do not modify them:

- Project, service, product, brand, and company names.
- API, SDK, protocol, standard, and formal specification names.
- CLI commands and arguments.
- Code and inline code.
- Shell commands.
- File and directory paths.
- URLs.
- Environment variables.
- Field names and schema keys.
- Program identifiers such as classes, functions, methods, and variables.
- Issue, task, test, requirement, and similar identifiers.
- Commit hashes.
- Version numbers.
- Error codes.
- Numbers and units.
- Placeholders, template tokens, and format strings.
- Markdown link destinations.
- Quoted text the user requires to remain verbatim.

Examples include `docker build`, `--no-cache`, `C:\Projects\example`, `/var/log`, `OPENAI_API_KEY`, `REQ-123`, `REP_B02`, `v1.2.3`, and `if (healthcheck)`.

Do not change these literals simply because they contain ordinary English words.

## Localization decisions

### General prose

Prefer natural Chinese equivalents for English conjunctions, function words, and ordinary prose that can be safely rewritten inside otherwise Chinese sentences.

For example, “A and B 都通過” may become “A 與 B 都通過”. However, do not change `and` when it appears inside code, a command, an official name, or another protected literal.

### Technical terminology

Technical concepts with stable and natural Chinese usage may be localized.

Keep the English term when the domain normally uses English directly, the Chinese translation is unstable, the translation could be confused with another concept, or the English wording materially improves technical precision.

Do not use a fixed dictionary to perform mechanical word-for-word substitution.

### Proper nouns and abbreviations

Preserve brands, product names, official standard names, and indivisible proper nouns by default. Do not automatically expand abbreviations.

Add a Chinese explanation only when the user asks, when omission would materially hinder understanding, or when the context clearly requires a first-use definition. Never guess an uncertain abbreviation expansion or translation.

## Workflow

1. Identify the requested editing scope and any established terminology conventions.
2. Identify and protect all exact literals that must not change.
3. Rewrite the remaining prose by sentence and meaning, not by word-for-word translation.
4. Verify meaning, logic, protected literals, and terminology consistency after editing.

If an English term cannot be safely localized without changing technical meaning, keep the original term.

## Fidelity rules

The revision must not:

- Add facts that were not in the source.
- Remove required conditions.
- Change negation.
- Change the scope of a condition.
- Change numbers, versions, or identifiers.
- Turn a recommendation into a completed action.
- Turn a possibility into a certainty.
- Mistake a technical name for ordinary English that should be translated.
- Rewrite code or commands for the sake of localization.

When natural Chinese and technical precision conflict, prioritize technical precision.

## Preserve formatting

Unless the user requests reformatting, preserve the existing Markdown hierarchy, lists, tables, code blocks, quotations, links, and paragraph logic as much as possible.

Punctuation, spacing, and sentence structure may be adjusted for natural Chinese reading, but the underlying data structure must remain intact.

## Acceptance checks

Before returning the result, confirm that:

- The main content reads as natural Traditional Chinese rather than literal translation.
- Unnecessary Chinese-English mixing has been reduced.
- Required English terms and exact literals were not changed accidentally.
- Technical terminology fits the context.
- The same concept uses consistent terminology throughout the document.
- Facts, conditions, negation, numbers, and logic remain unchanged.
- No awkward or incorrect translation was introduced merely to make the text “all Chinese.”

## Output

By default, return the complete revised version directly.

Do not automatically append a sentence-by-sentence change log, explanation, or glossary. Add explanation only when the user asks for it, when a material ambiguity could affect technical meaning, or when a term cannot be resolved safely.

When an ambiguity is unavoidable, preserve the original term rather than guessing a translation.