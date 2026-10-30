import test from 'node:test';
import assert from 'node:assert/strict';
import {WATER_CANDIDATES} from '../dist/water-candidates.mjs';
import {canRoute,validCoordinate} from '../dist/core.mjs';
test('published OSM candidates never bypass the real-water verification gate',()=>{
  assert.ok(WATER_CANDIDATES.length>0);
  for(const point of WATER_CANDIDATES){
    assert.ok(validCoordinate(point));
    assert.equal(point.demo,false);
    assert.equal(point.status,'candidate');
    assert.equal(point.checkedAt,null);
    assert.equal(canRoute(point,false),false);
    assert.equal(canRoute(point,true),false);
    assert.match(point.source,/^https:\/\/www\.openstreetmap\.org\/node\/\d+$/);
  }
});
