from flask import Flask, render_template, request
import random
from pyngrok import ngrok

app = Flask(__name__)

# Set up Ngrok authentication
ngrok.set_auth_token("2srLW734kc8vL62JpVLGfNRxZnz_6haawMvQcLm4ZL2VyjZwV")  # Replace with your actual Ngrok auth token
public_url = ngrok.connect(5000).public_url
print(f"Public URL: {public_url}")

@app.route('/')
def home():
        return '''
    <html>
    <head>
        <title>💌 A Journey to Forever 💌</title>
        <style>
            body {
                text-align: center;
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #ffefeb 0%, #ffd5e1 100%);
                margin: 0;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .container {
                background: rgba(255, 255, 255, 0.9);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 10px 30px rgba(255, 105, 180, 0.2);
                max-width: 800px;
                margin: 20px;
            }
            h1 {
                color: #ff4d94;
                font-size: 2.5em;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
                margin-bottom: 30px;
            }
            p {
                color: #666;
                font-size: 1.2em;
                line-height: 1.6;
                margin-bottom: 30px;
            }
            .gradient-heart {
                display: inline-block;
                padding: 20px 40px;
                font-size: 1.3em;
                font-weight: bold;
                color: white;
                background: linear-gradient(45deg, #ff6b6b, #ff8585);
                border: none;
                border-radius: 50px;
                cursor: pointer;
                transition: all 0.3s ease;
                text-decoration: none;
                box-shadow: 0 5px 15px rgba(255, 107, 107, 0.4);
            }
            .gradient-heart:hover {
                transform: translateY(-3px) scale(1.05);
                box-shadow: 0 8px 20px rgba(255, 107, 107, 0.6);
            }
            .floating-hearts {
                position: fixed;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: -1;
            }
        </style>
    </head>
    <body>
        <div class="floating-hearts" id="hearts"></div>
        <div class="container">
            <h1>💖 Your love quest begins here! 💖</h1>
            
            <p>💖 Some things in life are simply meant to be —like you and me.
            Every moment with you feels like a warm embrace, a soft melody that lingers, a story I never want to end. No matter where life takes us, know that my heart is always yours, wrapped in love, laughter, and a little bit of magic. </p>

            <p>💕 Close your eyes, take a breath, and step forward—something special awaits you. 💕</p>
            <a href='/road-crossing' class='gradient-heart' onclick="startMusic()">
                💖 Begin the Story 💖
            </a>
        </div>
        <audio id="endMusic" autoplay loop>
    <source src="https://www.bensound.com/bensound-music/bensound-love.mp3" type="audio/mpeg">
</audio>

        <script>
            function createHeart() {
                const heart = document.createElement('div');
                heart.innerHTML = '💖';
                heart.style.position = 'fixed';
                heart.style.left = Math.random() * 100 + 'vw';
                heart.style.top = '-20px';
                heart.style.fontSize = (Math.random() * 20 + 10) + 'px';
                heart.style.animation = `float ${Math.random() * 5 + 3}s linear infinite`;
                heart.style.opacity = '0.6';
                document.getElementById('hearts').appendChild(heart);
                setTimeout(() => heart.remove(), 8000);
            }
            
            setInterval(createHeart, 300);
            
            document.styleSheets[0].insertRule(`
                @keyframes float {
                    0% { transform: translateY(0) rotate(0deg); }
                    100% { transform: translateY(100vh) rotate(360deg); }
                }
            `, 0);
        </script>
    </body>
    </html>
    '''

@app.route('/road-crossing')
def road_crossing():
    return '''
   <html>
   <head>
    <title>🌸 Love's Garden 🌸</title>
    <style>
        body {
            text-align: center;
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #e0ffe0 0%, #d5f5ff 100%);
            margin: 0;
            min-height: 100vh;
            padding: 20px;
        }
        .game-container {
            background: rgba(255, 255, 255, 0.9);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(73, 182, 77, 0.2);
            max-width: 800px;
            margin: 0 auto;
        }
        canvas {
            background: linear-gradient(to bottom, #87CEEB, #98FB98);
            border: 3px solid #4CAF50;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            display: none;
            margin: 20px auto;
        }
        h2 {
            color: #2E7D32;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
        }
        p {
            color: #444;
            font-size: 1.1em;
            line-height: 1.6;
            margin: 20px 0;
        }
        button {
            padding: 15px 30px;
            font-size: 1.1em;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 10px;
        }
        #startGameBtn {
            background: linear-gradient(45deg, #4CAF50, #45a049);
            color: white;
            box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
        }
        #nextGameBtn {
            display: none;
            background: linear-gradient(45deg, #FF69B4, #FF1493);
            color: white;
            box-shadow: 0 4px 15px rgba(255, 105, 180, 0.3);
        }
        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
        }
        .love-message {
            font-size: 1.2em;
            color: #FF1493;
            margin: 20px 0;
            display: none;
        }
    </style>
</head>
<body>
    <div class="game-container">
        <h2>🌸 My Garden of Love 🌸</h2>
        <p>💐 Love blooms where you are… but extra flowers wouldn’t hurt. 😉🌸 Collect as many flowers as you can 💐 💝</p>
        <p class="instructions">Use arrow keys to move and collect as many flowers as you can! 🌺</p>
        <button id="startGameBtn">Start Collecting! 🎮</button>
        <canvas id="gameCanvas" width="500" height="500"></canvas>
        <p id="scoreDisplay" style="display: none; font-size: 20px; font-weight: bold;">You collected <span id="finalScore"></span> flowers! 🌸</p>
        <div id="loveMessage" class="love-message"></div>
        <button id="nextGameBtn" onclick="location.href='/ice-cream-catcher'">Next: Sweet Treats Await! 🍨</button>
    </div>
  

    <script>
        const canvas = document.getElementById("gameCanvas");
        const ctx = canvas.getContext("2d");
        const startBtn = document.getElementById("startGameBtn");
        
        let player = { x: 250, y: 450, size: 30, speed: 20, trail: [] };
        let flowers = ["🌸", "🌺", "🌼", "🌻", "💐"];
        let flowerPositions = [];
        let score = 0;
        let gameRunning = false;
        let gameTimer;

        function startGame() {
            canvas.style.display = "block";
            startBtn.style.display = "none";
            gameRunning = true;
            score = 0;
            player.trail = [];
            flowerPositions = [];
            
            // Initialize flowers
            for (let i = 0; i < 5; i++) {
                spawnFlower();
            }
            
            // Start game loop
            gameLoop();
            
            // Set game timer
            gameTimer = setTimeout(endGame, 20000);
        }

        function spawnFlower() {
            flowerPositions.push({
                x: Math.random() * (canvas.width - 40),
                y: Math.random() * (canvas.height - 40),
                flower: flowers[Math.floor(Math.random() * flowers.length)]
            });
        }

        function gameLoop() {
            if (!gameRunning) return;
            drawGame();
            requestAnimationFrame(gameLoop);
        }

        function drawGame() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Draw player and trail
            ctx.font = "30px Arial";
            player.trail.forEach((f, i) => {
                ctx.fillText(f, player.x - i * 20, player.y);
            });
            ctx.fillText("🙆🏻", player.x, player.y);
            
            // Draw flowers
            flowerPositions.forEach(flower => {
                ctx.fillText(flower.flower, flower.x, flower.y);
            });
        }

        function checkCollisions() {
            flowerPositions.forEach((flower, index) => {
                if (Math.abs(player.x - flower.x) < 30 && Math.abs(player.y - flower.y) < 30) {
                    player.trail.push(flower.flower);
                    flowerPositions.splice(index, 1);
                    score += 1;
                    spawnFlower();
                }
            });
        }

        function handleMovement(event) {
            if (!gameRunning) return;
            
            switch(event.key) {
                case "ArrowUp":
                    if (player.y > 30) player.y -= player.speed;
                    break;
                case "ArrowDown":
                    if (player.y < canvas.height - 30) player.y += player.speed;
                    break;
                case "ArrowLeft":
                    if (player.x > 30) player.x -= player.speed;
                    break;
                case "ArrowRight":
                    if (player.x < canvas.width - 30) player.x += player.speed;
                    break;
            }
            
            checkCollisions();
            event.preventDefault();
        }

        function endGame() {
            gameRunning = false;
            clearTimeout(gameTimer);
            
            let message;
            if (score >= 15) {
                message = "💝 Wow! You collected " + score + " flowers! Your love makes my garden bloom! 💝";
            } else if (score >= 10) {
                message = "💖 " + score + " beautiful flowers! Just like the beauty you bring to my life! 💖";
            } else {
                message = "💗 " + score + " lovely flowers! Each one as special as your smile! 💗";
            }
            
            document.getElementById("scoreDisplay").style.display = "block";
            document.getElementById("scoreDisplay").innerText = message;
            document.getElementById("loveMessage").style.display = "block";
            document.getElementById("nextGameBtn").style.display = "block";
        }

        // Event Listeners
        startBtn.addEventListener("click", startGame);
        document.addEventListener("keydown", handleMovement);
        
        // Initialize canvas size
        canvas.width = 500;
        canvas.height = 500;
    </script>
</body>
</html>
    '''

@app.route('/ice-cream-catcher')
def ice_cream_catcher():
 return '''
   <html>
<head>
    <title>🍦 Sweet Treats Catcher</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

        body {
            text-align: center;
            background: linear-gradient(135deg, #ffd1dc, #e0f7fa);
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        h2 {
            color: #ff6b6b;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        .game-container {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            margin: 20px auto;
        }

        canvas {
            background: linear-gradient(180deg, #87CEEB 0%, #e0f7fa 100%);
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        .btn {
            padding: 12px 24px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-family: 'Arial', sans-serif;
            font-size: 18px;
            transition: transform 0.2s, box-shadow 0.2s;
            margin: 10px;
        }

        #startGameBtn {
            background: linear-gradient(45deg, #ff6b6b, #ffd1dc);
            color: white;
        }

        #nextGameBtn {
            background: linear-gradient(45deg, #ff8fab, #ffc2d1);
            color: white;
            display: none;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }

        #scoreDisplay {
            display: none;
            font-size: 24px;
            color: #ff6b6b;
            margin: 20px 0;
            animation: popIn 0.5s ease-out;
        }

        .intro-text {
            color: #666;
            font-size: 18px;
            margin-bottom: 20px;
            line-height: 1.5;
        }

        @keyframes popIn {
            0% { transform: scale(0.8); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }

        .controls-info {
            color: #666;
            font-size: 16px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h2>🍦 Sweet Treats Catcher 🍩</h2>
    <p class="intro-text"> Catch these treats before they melt—just like my heart when I see you! 🍦💕</p>
    <div class="game-container">
        <button id="startGameBtn" class="btn">Start Game 🎮</button>
        <canvas id="gameCanvas" width="400" height="400" style="display: none;"></canvas>
        <p class="controls-info">Use ← → arrow keys to move</p>
        <div id="scoreDisplay">
            <p>💘 You caught <span id="finalScore"></span> treats! 💘</p>
            <p>"Each treat caught = one reason to love you more! 😘"</p>
        </div>
        <button id="nextGameBtn" class="btn">Next: A Love Challenge! 💖</button>

    </div>


    <script>
        let canvas = document.getElementById("gameCanvas");
        let ctx = canvas.getContext("2d");
        let catcher = { x: 150, y: 350, width: 80, height: 80 };
        let foods = ["🍦", "🍩", "🥐", "🍫", "🍪"];
        let fallingItems = [];
        let score = 0;
        let gameTime = 30;
        let gameRunning = false;
        let timerInterval;

        function startGame() {
            document.getElementById("startGameBtn").style.display = "none";
            canvas.style.display = "block";
            gameRunning = true;
            score = 0;
            gameTime = 30;
            spawnFood();
            requestAnimationFrame(gameLoop);
            timerInterval = setTimeout(endGame, gameTime * 1000);
        }

        function spawnFood() {
            fallingItems.push({
                x: Math.random() * 370,
                y: -30,
                ySpeed: 2 + Math.random() * 1.5, // Slower falling speed
                rotation: Math.random() * 360,
                item: foods[Math.floor(Math.random() * foods.length)]
            });
            if (gameRunning) setTimeout(spawnFood, 1500);
        }

        function gameLoop() {
            if (!gameRunning) return;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Draw catcher
            ctx.save();
            ctx.shadowColor = 'rgba(0, 0, 0, 0.2)';
            ctx.shadowBlur = 5;
            ctx.shadowOffsetY = 2;
            ctx.font = "40px Arial";
            ctx.fillText("💁🏻", catcher.x, catcher.y);
            ctx.restore();

            // Draw falling items
            fallingItems.forEach((food, index) => {
                food.y += food.ySpeed;
                food.rotation += 2;
                
                ctx.save();
                ctx.translate(food.x + 15, food.y);
                ctx.rotate(food.rotation * Math.PI / 180);
                ctx.font = "30px Arial";
                ctx.fillText(food.item, -15, 0);
                ctx.restore();

                if (food.y >= catcher.y - 30 && food.y <= catcher.y + 30 &&
                    food.x >= catcher.x - 30 && food.x <= catcher.x + 30) {
                    fallingItems.splice(index, 1);
                    score++;
                }

                if (food.y > canvas.height + 30) {
                    fallingItems.splice(index, 1);
                }
            });

            requestAnimationFrame(gameLoop);
        }

        function move(event) {
            if (!gameRunning) return;
            if (event.key === "ArrowLeft" && catcher.x > 0) catcher.x -= 20;
            if (event.key === "ArrowRight" && catcher.x < canvas.width - catcher.width) catcher.x += 20;
        }

        function endGame() {
            gameRunning = false;
            clearTimeout(timerInterval);
            document.getElementById("finalScore").innerText = score;
            document.getElementById("scoreDisplay").style.display = "block";
            document.getElementById("nextGameBtn").style.display = "block";
        }

        document.getElementById("startGameBtn").onclick = startGame;
        document.getElementById("nextGameBtn").onclick = () => location.href = '/flappy-love';
        document.addEventListener("keydown", move);
    </script>
</body>
</html>
    '''

@app.route('/flappy-love')
def flappy_love():
    return '''
<html>
<head>
    <title>💖 Flappy Love 💖</title>
    <style>
        body { 
            text-align: center; 
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom, #ffe6f2, #ffb3d9);
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }
        canvas { 
            background: linear-gradient(to bottom, #87CEEB, #e6f7ff);
            border: 3px solid #ff66b2;
            border-radius: 10px;
            display: block; 
            margin: 20px auto;
            width: 700px; 
            height: 400px;
            box-shadow: 0 0 20px rgba(255, 102, 178, 0.3);
        }
        h2 {
            color: #ff1a75;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        p {
            color: #ff4d94;
            font-size: 18px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h2>💖 Jump through the hurdles of love! 💖</h2>
    <p>Press the spacebar to flap and avoid obstacles. Jump through the hurdles of love! But don’t trip—you’re already falling for me. 😉💘 </p>
    <button id="startGameBtn" style="padding: 12px 24px; background: #ff66b2; color: white; border: none; border-radius: 8px; font-size: 18px; cursor: pointer;">Start Game 🎮</button>

    <canvas id="gameCanvas" width="600" height="400"></canvas>
    <script>
        let canvas = document.getElementById("gameCanvas");
        let ctx = canvas.getContext("2d");
        let startBtn = document.getElementById("startGameBtn");
        let boy = { x: 50, y: 200, velocity: 0, gravity: 0.4, lift: -8, score: 0 }; // Reduced gravity and lift for smoother movement
        let princess = { x: 550, y: 200 };
        let obstacles = [];
        let hearts = [];
        let clouds = [];
        let gameRunning = false;
        let gameTime = 30; 
        let reachedPrincess = false;

        function drawCloud(x, y) {
            ctx.fillStyle = "rgba(255, 255, 255, 0.8)";
            ctx.beginPath();
            ctx.arc(x, y, 20, 0, Math.PI * 2);
            ctx.arc(x + 15, y - 10, 15, 0, Math.PI * 2);
            ctx.arc(x + 15, y + 10, 15, 0, Math.PI * 2);
            ctx.arc(x + 30, y, 20, 0, Math.PI * 2);
            ctx.fill();
        }
        

        function drawGame() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            // Draw clouds
            clouds.forEach(cloud => {
                drawCloud(cloud.x, cloud.y);
                cloud.x -= 1; // Move clouds slowly
            });

            // Draw boy with slight animation
            ctx.font = "40px Arial";
            ctx.fillText("🥷🏻", boy.x, boy.y);

            // Draw princess with a heart above
            ctx.fillText("👸🏻", princess.x, princess.y);
            ctx.fillText("💝", princess.x, princess.y - 40);

            // Draw obstacles with gradient
            obstacles.forEach(obstacle => {
                let gradient = ctx.createLinearGradient(obstacle.x, 0, obstacle.x + 60, 0);
                gradient.addColorStop(0, "#ff99cc");
                gradient.addColorStop(1, "#ff66b2");
                ctx.fillStyle = gradient;
                ctx.fillRect(obstacle.x, obstacle.y, 60, obstacle.height);
            });

            // Draw hearts with glow effect
            ctx.shadowBlur = 10;
            ctx.shadowColor = "rgba(255, 102, 178, 0.5)";
            hearts.forEach(heart => {
                ctx.fillText("💗", heart.x, heart.y);
            });
            ctx.shadowBlur = 0;

            // Draw score and time
            ctx.font = "24px Arial";
            ctx.fillStyle = "#ff1a75";
            ctx.fillText("Hearts: " + boy.score, 20, 40);
            ctx.fillText("Time: " + gameTime + "s", canvas.width - 120, 40);
        }

          function startGame() {
            startBtn.style.display = "none"; // Hide start button
            canvas.style.display = "block"; // Show game
            gameRunning = true;
            spawnObstacle();
            spawnHeart();
            spawnClouds();
            countdown();
            drawGame();
            moveBoy();
        }

        function moveBoy() {
            if (!gameRunning) return;
            boy.velocity += boy.gravity;
            boy.y += boy.velocity;
            
            // Check for princess collision
            if (Math.abs(boy.x - princess.x) < 30 && Math.abs(boy.y - princess.y) < 30 && !reachedPrincess) {
                boy.score += 3; // Bonus hearts
                reachedPrincess = true;
                endGame();
                return;
            }

            // Boundary checks
            if (boy.y > canvas.height - 30 || boy.y < 0) {
                endGame();
                return;
            }

            // Obstacle collision
            obstacles.forEach((obstacle, index) => {
                obstacle.x -= 4;
                if (obstacle.x < -60) obstacles.splice(index, 1);
                if (boy.x > obstacle.x && boy.x < obstacle.x + 60 && boy.y > obstacle.y && boy.y < obstacle.y + obstacle.height) {
                    endGame();
                    return;
                }
            });

            // Heart collection
            hearts.forEach((heart, index) => {
                heart.x -= heart.speed;
                if (heart.x < -30) hearts.splice(index, 1);
                if (Math.abs(boy.x - heart.x) < 30 && Math.abs(boy.y - heart.y) < 30) {
                    boy.score += 1;
                    hearts.splice(index, 1);
                }
            });

            drawGame();
            requestAnimationFrame(moveBoy);
        }

        function flap(event) {
            if (!gameRunning) return;
            if (event.code === "Space") {
                boy.velocity = boy.lift;
                event.preventDefault();
            }
        }

        function spawnObstacle() {
            let height = Math.random() * 150 + 50;
            let gap = 140; // Increased gap
            let positionY = Math.random() * (canvas.height - height - gap);
            obstacles.push({ x: canvas.width, y: 0, height: positionY });
            obstacles.push({ x: canvas.width, y: positionY + gap, height: canvas.height - positionY - gap });
            if (gameRunning) setTimeout(spawnObstacle, 2000);
        }

        function spawnHeart() {
            let positionY = Math.random() * (canvas.height - 40);
            hearts.push({ x: canvas.width, y: positionY, speed: Math.random() * 2 + 2 });
            if (gameRunning) setTimeout(spawnHeart, 1500);
        }

        function spawnClouds() {
            clouds.push({ x: canvas.width + 30, y: Math.random() * 150 + 50 });
            if (gameRunning) setTimeout(spawnClouds, 3000);
        }

function endGame() {
    gameRunning = false;

    let heartIcons = "💖".repeat(Math.min(boy.score, 30));

    setTimeout(() => {
        document.body.innerHTML = `
            <div style="padding: 40px; background: white; border-radius: 20px; box-shadow: 0 0 30px rgba(255, 102, 178, 0.3); max-width: 600px; margin: 40px auto; text-align: center; position: relative;">
                <h2>💖 Will you be my Valentine? 💖</h2>
                <h3 style="color: #ff4d94;">I promise to love you ${heartIcons} much! </h3>
                <button id="yesButton" style="padding: 10px 20px; background: #ff66b2; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 18px;">YES</button>
                <div id="restartContainer" style="margin-top: 20px; display: none;">
                    <button id="tryAgainButton" style="padding: 10px 20px; background: #ff4081; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 18px;">Try Again</button>
                </div>
            </div>

            <style>
                .falling-heart {
                    position: fixed;
                    top: -50px;
                    font-size: 30px;
                    animation: fall 4s linear infinite;
                    color: #ff4d94;
                }
                @keyframes fall {
                    0% { transform: translateY(0); opacity: 1; }
                    100% { transform: translateY(100vh); opacity: 0; }
                }
            </style>
        `;

        document.getElementById("yesButton").addEventListener("click", () => {
            setInterval(createHeart, 300);
            document.getElementById("yesButton").style.display = "none"; // Hide YES button

            // Show "Try Again" button after 10s
            setTimeout(() => {
                document.getElementById("restartContainer").style.display = "block";
            }, 5000);
        });

        document.getElementById("tryAgainButton").addEventListener("click", () => {
            location.reload(); // Reload the page when "Try Again" is clicked
        });

    }, 1000);
}

function createHeart() {
    let heart = document.createElement("div");
    heart.className = "falling-heart";
    heart.innerHTML = "💓";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = (Math.random() * 2 + 2) + "s";
    document.body.appendChild(heart);
    setTimeout(() => heart.remove(), 4000);
}



        function countdown() {
            if (gameTime > 0 && gameRunning) {
                gameTime--;
                setTimeout(countdown, 1000);
            } else if (gameRunning) {
                endGame();
            }
        }

        document.addEventListener("keydown", flap);
        startBtn.addEventListener("click", startGame);

    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(port=5000)
