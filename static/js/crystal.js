/* Interactive ABO3 perovskite lattice — lazy-loaded, drag-to-rotate.
   Loads three.js only when the section scrolls into view. */
(function () {
  var wrap = document.getElementById('crystal-wrap');
  if (!wrap) return;

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var loaded = false, running = false, renderer, scene, camera, group, aSpheres = [];
  var doped = false;

  var GOLD = 0xd4af37, K_GREEN = 0x2ed573, B_BLUE = 0x4169aa, O_RED = 0xe74c3c;

  function loadThree(cb) {
    var s = document.createElement('script');
    s.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
    s.onload = cb;
    s.onerror = function () {
      wrap.innerHTML = '<p style="color:#888;text-align:center;padding:40px 0;">3D viewer unavailable — but the science still works. 🧪</p>';
    };
    document.head.appendChild(s);
  }

  function init() {
    if (typeof THREE === 'undefined') {
      wrap.innerHTML = '<p style="color:#888;text-align:center;padding:40px 0;">3D viewer unavailable — but the science still works. 🧪</p>';
      return;
    }
    var size = Math.min(wrap.clientWidth || 340, 440);
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(38, 1, 0.1, 100);
    camera.position.set(0, 0, 7);

    try {
      renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    } catch (err) {
      wrap.innerHTML = '<p style="color:#888;text-align:center;padding:40px 0;">Your browser blocked 3D rendering — but the science still works. 🧪</p>';
      return;
    }
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setSize(size, size);
    wrap.innerHTML = '';
    wrap.appendChild(renderer.domElement);
    renderer.domElement.style.cssText = 'cursor:grab;touch-action:none;max-width:100%;';

    scene.add(new THREE.AmbientLight(0xffffff, 0.55));
    var dl = new THREE.DirectionalLight(0xffffff, 0.9);
    dl.position.set(4, 6, 5);
    scene.add(dl);

    group = new THREE.Group();
    scene.add(group);

    function sphere(r, color, x, y, z) {
      var m = new THREE.Mesh(
        new THREE.SphereGeometry(r, 32, 32),
        new THREE.MeshPhongMaterial({ color: color, shininess: 60 })
      );
      m.position.set(x, y, z);
      group.add(m);
      return m;
    }

    // A-site cations: cube corners (La / K after doping)
    [-1, 1].forEach(function (x) {
      [-1, 1].forEach(function (y) {
        [-1, 1].forEach(function (z) {
          aSpheres.push(sphere(0.34, GOLD, x, y, z));
        });
      });
    });

    // B-site: center (Mn)
    sphere(0.26, B_BLUE, 0, 0, 0);

    // Oxygen: face centers
    var oPos = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]];
    oPos.forEach(function (p) { sphere(0.16, O_RED, p[0], p[1], p[2]); });

    // B–O bonds
    oPos.forEach(function (p) {
      var dir = new THREE.Vector3(p[0], p[1], p[2]);
      var bond = new THREE.Mesh(
        new THREE.CylinderGeometry(0.045, 0.045, 1, 12),
        new THREE.MeshPhongMaterial({ color: 0x8899aa })
      );
      bond.position.copy(dir.clone().multiplyScalar(0.5));
      bond.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), dir.clone().normalize());
      group.add(bond);
    });

    // Octahedron edges between adjacent oxygens
    var octaPts = [];
    for (var i = 0; i < oPos.length; i++) {
      for (var j = i + 1; j < oPos.length; j++) {
        var a = new THREE.Vector3().fromArray(oPos[i]);
        var b = new THREE.Vector3().fromArray(oPos[j]);
        if (Math.abs(a.distanceTo(b) - Math.SQRT2) < 0.01) octaPts.push(a, b);
      }
    }
    var octaGeo = new THREE.BufferGeometry().setFromPoints(octaPts);
    group.add(new THREE.LineSegments(octaGeo, new THREE.LineBasicMaterial({ color: 0x64b5f6, transparent: true, opacity: 0.5 })));

    // Unit-cell edges
    var box = new THREE.EdgesGeometry(new THREE.BoxGeometry(2, 2, 2));
    group.add(new THREE.LineSegments(box, new THREE.LineBasicMaterial({ color: 0xbbbbbb, transparent: true, opacity: 0.6 })));

    group.rotation.set(0.35, -0.6, 0);

    // Drag to rotate
    var dragging = false, px = 0, py = 0;
    var el = renderer.domElement;
    el.addEventListener('pointerdown', function (e) {
      dragging = true; px = e.clientX; py = e.clientY;
      el.style.cursor = 'grabbing'; el.setPointerCapture(e.pointerId);
    });
    el.addEventListener('pointermove', function (e) {
      if (!dragging) return;
      group.rotation.y += (e.clientX - px) * 0.008;
      group.rotation.x += (e.clientY - py) * 0.008;
      group.rotation.x = Math.max(-1.4, Math.min(1.4, group.rotation.x));
      px = e.clientX; py = e.clientY;
    });
    ['pointerup', 'pointercancel', 'pointerleave'].forEach(function (ev) {
      el.addEventListener(ev, function () { dragging = false; el.style.cursor = 'grab'; });
    });

    window.addEventListener('resize', function () {
      var s = Math.min(wrap.clientWidth, 440);
      renderer.setSize(s, s);
    });

    window.__crystalTick = function tick() {
      if (!running) { window.__crystalAnimating = false; return; }
      if (!dragging && !reducedMotion) group.rotation.y += 0.004;
      renderer.render(scene, camera);
      requestAnimationFrame(tick);
    };
    running = true;
    window.__crystalAnimating = true;
    window.__crystalTick();

    // Doping toggle
    var btn = document.getElementById('dope-btn');
    var cap = document.getElementById('crystal-caption');
    if (btn) btn.addEventListener('click', function () {
      doped = !doped;
      [0, 5].forEach(function (i) { aSpheres[i].material.color.setHex(doped ? K_GREEN : GOLD); });
      btn.textContent = doped ? '↺ Restore pure LaMnO₃' : '⚗️ Substitute K⁺ — my Ph.D. trick';
      if (cap) cap.innerHTML = doped
        ? '<strong>K-substituted LaMnO₃</strong> — swapping La³⁺ (gold) for K⁺ (green) creates the defects that made my zinc–air battery catalyst survive 1000+ cycles.'
        : '<strong>LaMnO₃ perovskite (ABO₃)</strong> — gold: La³⁺ (A-site) · blue: Mn (B-site) · red: O²⁻ octahedron. Drag to rotate.';
    });
  }

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) {
        if (!loaded) { loaded = true; loadThree(init); }
        else if (renderer && !window.__crystalAnimating) {
          running = true;
          window.__crystalAnimating = true;
          window.__crystalTick();
        }
      } else {
        running = false;
      }
    });
  }, { threshold: 0.15 });
  io.observe(wrap);
})();
