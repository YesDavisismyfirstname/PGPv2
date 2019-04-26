var height = window.innerHeight;
var width = window.innerWidth;
var scene, camera, renderer
var container



function init() {
    container = document.createElement('div');
    document.body.appendChild(container);


    camera = new THREE.PerspectiveCamera(70, width, height, 1, 2000)
    camera.position.set(0,-40,50);

    scene = new THREE.Scene()

    renderer = new THREE.WebGLRenderer();
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(width, height);

    var planeGeometry = new THREE.PlaneGeometry(10, 20, 32);
    var planeMaterial = new THREE.MeshBasicMaterial( {color: 0xffff00});
    var plane = new THREE.Mesh(planeGeometry, planeMaterial);
    plane.position.set(0,0,-1);
    scene.add(plane)
    
    var loader = new THREE.ObjectLoader()
    loader.load("apps\game_window\static\game_window\images\bulbasaur\Bulbasaur.obj",    
	function ( object ) {
		scene.add( object );

    })



}

function renderScene(){
    requestAnimationFrame.AnimationFrame(renderScene);
    renderer.render(scene, camera);
}


init();
renderScene();
