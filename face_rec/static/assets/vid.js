const video = document.querySelector('video');
const models = 'https://luisarmando-testcoder.github.io/QuickerJs/lib/face-api.min/weights';

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri(models),
  faceapi.nets.faceLandmark68Net.loadFromUri(models),
  faceapi.nets.faceRecognitionNet.loadFromUri(models),
  faceapi.nets.faceExpressionNet.loadFromUri(models)
]).then(startVideo);

function startVideo() {
  navigator.getUserMedia(
    {video: {}},
    stream =>  video.srcObject = stream,
    err => console.error(err)
  );
}

video.addEventListener('play', e => {
  const displaySize = { width: video.width, height: video.height};
  const canvas = faceapi.createCanvasFromMedia(video);
  const ctx = canvas.getContext('2d');
  document.body.append(canvas);
  faceapi.matchDimensions(canvas, displaySize);
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions())
      .withFaceLandmarks()
      .withFaceExpressions();
    const resizedDetections = faceapi.resizeResults(detections, displaySize);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    faceapi.draw.drawFaceLandmarks(canvas, resizedDetections);
    faceapi.draw.drawFaceExpressions(canvas, resizedDetections);
  });
});