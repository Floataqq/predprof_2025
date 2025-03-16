import * as THREE from 'three';
import { MapControls } from 'three/addons/controls/MapControls.js';
import * as BufferGeometryUtils from 'three/addons/utils/BufferGeometryUtils.js';

async function get_data() {
  const json_data = await fetch('/data')
  const data = await json_data.json()
  return data;
}

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 
                                            0.1, 1000 );
const renderer = new THREE.WebGLRenderer();
const controls = new MapControls(camera, renderer.domElement);
const tiles = [];
controls.enableDamping = true; // an animation loop is required when either damping or auto-rotation are enabled
controls.dampingFactor = 0.05;

controls.screenSpacePanning = false;

controls.minDistance = 20;
controls.maxDistance = 500;

controls.maxPolarAngle = Math.PI / 2;

renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

function normalize(c, factor) {
  return Math.floor(c * (factor + 25) / 255);
}

function place_tile(x, y, height) {
  const geometry = new THREE.BoxGeometry( 1, 5 * height / 255, 1 );
  geometry.translate(x, 5 * height / 255 / 2, y);
  // tiles.push(geometry);
  const color = normalize(0xdb, height) * 0x10000 + normalize(0x42, height) * 0x100 + normalize(0x2c, height);
  const material = new THREE.MeshBasicMaterial( { color } );
  const tile = new THREE.Mesh( geometry, material );
  scene.add(tile);
}

function animate() {
  controls.update();
  renderer.render(scene, camera);
}

const api_data = await get_data();
let data = [];
for (let e in api_data) {
  let block = api_data[e]['message']['data'];
  let new_block = [];
  for (let j = 0; j < 64; j+=2) {
    let new_row = [];
    for (let k = 0; k < 64; k+=2) {
      new_row.push(block[j][k]);
    }
    new_block.push(new_row);
  }
  data.push(new_block);
}

console.log(data);

let block_x = 0, block_y = 0;
for (let block in data) {
  let y = 0;
  for (let row of data[block]) {
    let x = 0;
    for (let height of row) {
      place_tile(block_x * 32 + x, block_y * 32 + y, height);
      x++;
    }
    y++;
  }
  block_x++;
  if (block_x % 4 == 0) { block_y += 1; block_x = 0; }
}

// const geom = BufferGeometryUtils.mergeGeometries(tiles);
// const material = new THREE.MeshNormalMaterial();
// scene.add(new THREE.Mesh(geom, material));

renderer.setAnimationLoop(animate);

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();

    renderer.setSize( window.innerWidth, window.innerHeight );
}

window.addEventListener( 'resize', onWindowResize );


