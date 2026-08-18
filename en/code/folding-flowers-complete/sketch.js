function setup() {
  createCanvas(400, 400);
  ellipseMode(CENTER);
  rectMode(CENTER);
  noStroke();
}

function draw() {
  // the paper
  background(255);
  fill(200, 30, 40);
  ellipse(200, 200, 300, 300);

  // the shapes cut out of the paper
  fill(255);
  ellipse(200, 120, 60, 60);
  rect(200, 215, 110, 40);
  triangle(165, 300, 235, 300, 200, 255);
}
