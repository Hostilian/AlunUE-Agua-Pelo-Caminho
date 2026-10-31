import test from 'node:test';
import assert from 'node:assert/strict';
import {foldText} from '../dist/core.mjs';

test('Portuguese discovery matches accents, decomposed text and case',()=>{
  const name='Água mapeada · perto da Praça de Giraldo';
  assert.ok(foldText(name).includes(foldText('AGUA')));
  assert.ok(foldText(name).includes(foldText('praca')));
  assert.equal(foldText(' A\u0301GUA '),foldText('água'));
  assert.equal(foldText(null),'');
});
