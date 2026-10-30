# Decisions and release gates

| Decision | Reason | Revisit when |
|---|---|---|
| Position as AlunUÉ mobility/essential-services module | Fits the retained student-life context more closely than a standalone tourism platform | Group/instructor scope is confirmed |
| Research report before product breadth | Phase 1 rubric rewards methodological rigour | Actual evidence is synthesised |
| Demo water by default, clear labels everywhere | No trusted inventory was found | Specific points have current evidence |
| No real-mode routing to OSM water candidates | Mapped is not equivalent to free, safe or working | Verification and freshness governance exist |
| Manual stop order first | User intent and mobile compatibility | A pedestrian route provider is selected |
| No account/backend for initial prototype | Lower friction, cost and exposure | Moderated shared reports/partners need persistence |
| No APK this evening | A signed native wrapper does not complete the research assignment | PWA tested; native benefit identified |
| No hidden purchases or shop promotion | A refill should remain free and voluntary | Merchant trial provides actual evidence |

## Operational acceptance gates

No operational launch before refill verification and expiry, report moderation, named data owner, partner agreements, real phone/accessibility QA, source licences, API usage review and a publicly usable hosting audience are resolved. These are product requirements, not claims that those actions have happened.

## Rollback

Keep versioned source and prior deployable snapshot. If trust metadata fails, hide water results and retain a clearly labelled empty state. If provider fails, display stale timestamp or an unavailable message, with no fake inventory. Roll back a deployment to the previous tested version if routing drops stops or demo data leaks into live journeys.
