function setup() {
  const canvas = createCanvas(400, 400);
  canvas.parent('sketch-holder');
  rectMode(CENTER);
  noStroke();
}

function draw() {
  // the paper
  background(255);
  fill(200, 30, 40);
  circle(200, 200, 300);

  // the shapes cut out of the paper
  fill(255);
  circle(200, 120, 60);
  rect(200, 215, 110, 40);
  triangle(165, 300, 235, 300, 200, 255);
}
