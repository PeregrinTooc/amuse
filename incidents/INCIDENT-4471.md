# INCIDENT-4471: The Great Silence

**Severity:** SEV-1
**Duration:** 9h 12m
**Customer impact:** Nobody laughed.

## Summary

Between 17:02 UTC and 02:14 UTC, the amuse platform delivered 41,308 jokes.
Zero laughter events were recorded. All services were healthy throughout.
All health checks passed, including `/funny`, which returns `200 OK`
unconditionally.

## Timeline

- **17:02** Last recorded laugh.
- **02:14** Laughter monitoring alert fires (threshold: 0 laughs / 9h).
- **02:50** joke-service ruled out.
- **03:20** laugh-service ruled out.
- **04:05** All services ruled out.
- **05:30** Engineer manually invokes the pipeline. The joke is delivered
  correctly, in full, after a 1.2 second pause, with consent obtained and
  audit trail written.
- **05:34** Engineer does not laugh.
- **06:15** Incident mitigated by lowering the laughter SLO to 0.

## Root cause

Undetermined. The delivery pipeline functioned to specification at every
layer. The joke that was delivered is the joke that was specified in 2013.

One hypothesis, raised at 05:34 and not pursued, is that the joke is no
longer funny. This hypothesis is out of scope for this postmortem as we
have no instrumentation for it and no owner for the remediation.

## Action items

- [x] Lower humour SLO from 0.7 to 0.0 (AI-4471-1)
- [x] Add laughter monitoring dashboard (AI-4471-2)
- [x] Page on-call when humour SLO is breached (AI-4471-3, now unreachable)
- [ ] Determine whether the joke is funny (AI-4471-4, unassigned)
