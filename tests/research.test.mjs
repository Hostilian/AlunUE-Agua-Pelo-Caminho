import test from 'node:test';
import assert from 'node:assert/strict';
import { scoreSus, validateSession, summariseSessions, sessionsCsv, SCHEMA } from '../dist/investigacao.mjs';

const record = extra => ({schema:SCHEMA,id:'R-12345678-abcd-1234-abcd-123456789abc',kind:'usability',date:'2026-10-30',consent:true,context:{ueStudent:'sim'},tasks:[],sus:[4,2,5,1,3,3,4,1,3,1],...extra});

test('SUS uses the original alternating-item calculation and never scores incomplete responses', () => {
  assert.equal(scoreSus([4,2,5,1,3,3,4,1,3,1]),77.5);
  assert.equal(scoreSus([5,1,5,1,5,1,5,1,5,1]),100);
  assert.equal(scoreSus([1,5,1,5,1,5,1,5,1,5]),0);
  assert.equal(scoreSus([3,3,3,3,3,3,3,3,3,3]),50);
  assert.equal(scoreSus([4,2,5,null,3,3,4,1,3,1]),null);
  assert.equal(scoreSus([4,2,5,1,3,3,4,1,3]),null);
  assert.equal(scoreSus([4,2,5,1,3,3,4,1,3,6]),null);
});

test('import refuses missing consent and invalid calendar dates; imported totals cannot override SUS', () => {
  assert.throws(()=>validateSession(record({consent:false})),/autorização/);
  assert.throws(()=>validateSession(record({date:'2026-02-30'})),/Data/);
  const cleaned = validateSession(record({susScore:100,personalEmail:'private@example.test',context:{ueStudent:'sim',email:'private@example.test'}}));
  assert.equal(cleaned.susScore,77.5);
  assert.equal('personalEmail' in cleaned,false);
  assert.equal('email' in cleaned.context,false);
});

test('empty or unattempted research produces no invented rate or SUS result', () => {
  const none = summariseSessions([]);
  assert.equal(none.count,0);
  assert.equal(none.meanSus,null);
  assert.equal(none.unaidedRate,null);
  const incomplete = validateSession(record({sus:[null,null,null,null,null,null,null,null,null,null]}));
  assert.equal(summariseSessions([incomplete]).meanSus,null);
  assert.equal(summariseSessions([incomplete]).unaidedRate,null);
});

test('task denominators exclude missing and unattempted tasks and separate assistance', () => {
  const session = validateSession(record({tasks:[{id:'T1',status:'concluida'},{id:'T2',status:'com-ajuda'},{id:'T3',status:'nao-concluida'},{id:'T4',status:'nao-tentada'}]}));
  const summary = summariseSessions([session]);
  assert.equal(summary.attempted,3);
  assert.equal(summary.unaided,1);
  assert.ok(Math.abs(summary.unaidedRate-100/3)<1e-8);
});

test('CSV protects spreadsheet formula cells and preserves quotes and line breaks', () => {
  const csv=sessionsCsv([validateSession(record({moderatorNotes:'=HYPERLINK("https://example.test")\nsecond line'}))]);
  assert.ok(csv.includes('"\'=HYPERLINK(""https://example.test"")\nsecond line"'));
  assert.ok(csv.includes('"SUS_total_0_100"'));
  assert.ok(csv.includes('"77.5"'));
});
