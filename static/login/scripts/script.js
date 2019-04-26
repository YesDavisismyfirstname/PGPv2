
//Navigation Functions

$('document').ready(function () {

	//startpage
	

	
});
/*

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
var loader = new THREE.OBJLoader()
var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var geometry = new THREE.BoxGeometry( 1, 1, 1 );
var material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
var cube = new THREE.Mesh( geometry, material );
scene.add( cube );

camera.position.z = 10;
camera.position.y = 5;
var light = new THREE.DirectionalLight( 0xffffff, 1, 100 );
light.position.set( -5, 5, 10 );
scene.add( light)
loader.load("../static/images/models/bulbasaur/bulbasaur.obj",
        // onLoad callback
	// Here the loaded data is assumed to be an object
	function ( object ) {

		scene.add( object );

	},
	// called when loading is in progresses
	function ( xhr ) {

		console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' );

	},
	// called when loading has errors
	function ( error ) {

		console.log( 'An error happened' );

	}
);
function animate() {
    requestAnimationFrame( animate );
    cube.rotation.x += 0.01;
cube.rotation.y += 0.01;
	renderer.render( scene, camera );
}
animate()*/