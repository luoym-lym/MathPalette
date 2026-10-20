# Frontend regression checks

The browser test file uses an in-memory synthetic API and a temporary local static server. It does not call the review backend or read/write candidate records. All Pass/Delete operations in this suite affect only synthetic JavaScript objects.

## Pure logic and packaged metadata

```sh
node --test review_workbench/tests/test_review_core.cjs
node --check review_workbench/static/app.js
node --check review_workbench/static/review-core.js
```

The pure tests cover state normalization, filters, progress, next-item selection, source/candidate option values, nested verification schemas, source corrections, exact-versus-numeric answers, and extraction of available verification explanations from all currently pending candidates. The packaged-data test is read-only.

## Synthetic browser scenarios

Requires the official Playwright Node package and an installed Chromium browser. Override `CHROMIUM_PATH` if necessary.

```sh
node --test review_workbench/tests/test_frontend.cjs
```

Scenarios:
- At most 40 list rows in the DOM, only two current images, and readable source/derived answers
- Double-click suppression and immediate busy controls
- Delete cancel, Escape, and explicit confirmation
- Failed Pass remains selected; retry reuses exactly the same fingerprint and request ID
- Pending request identity survives page reload
- Navigation while saving and late responses
- Navigating away and back while saving cannot approve the completed item again
- Late detail responses, browser Back, and reload selection
- The final pending item, empty state, and persisted history
- Input focus, image zoom, Escape, and focus restoration
- Untrusted source text, safe MathML, and broken-image approval blocking
- Mobile overflow and decision controls

The suite writes `.runtime/frontend-qa/frontend-desktop.png` and `.runtime/frontend-qa/frontend-mobile.png` as disposable screenshots. They are not part of the data library.

## Browser restrictions

Some execution sandboxes cannot launch Chromium because local browser sockets are restricted. A startup error is not a test pass. In that environment, run the same suite in the approved desktop/cloud-browser environment, or perform the equivalent manual browser scenarios on an isolated repository copy. Never perform destructive QA against the real candidate collection.
