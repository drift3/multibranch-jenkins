# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hello, World!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Cloud | DevOps Demo</title>
    <meta name="theme-color" content="#080d1b">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --bg: #080d1b;
            --card: rgba(18, 28, 49, 0.78);
            --blue: #62a8ff;
            --cyan: #53e5df;
            --text: #f1f5ff;
            --muted: #96a5bd;
            --border: rgba(148, 175, 220, 0.15);
        }

        body {
            min-height: 100vh;
            color: var(--text);
            font-family: Inter, "Segoe UI", Arial, sans-serif;
            background:
                radial-gradient(ellipse at 80% 20%,
                    rgba(42, 95, 180, .22), transparent 38%),
                radial-gradient(ellipse at 10% 90%,
                    rgba(30, 180, 190, .12), transparent 35%),
                var(--bg);
            overflow-x: hidden;
        }

        body::before {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            opacity: .16;
            background-image:
                linear-gradient(rgba(130,160,210,.08) 1px, transparent 1px),
                linear-gradient(90deg, rgba(130,160,210,.08) 1px, transparent 1px);
            background-size: 44px 44px;
        }

        .container {
            position: relative;
            width: min(1120px, 90%);
            margin: auto;
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 27px 0;
            border-bottom: 1px solid var(--border);
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 17px;
            font-weight: 800;
            letter-spacing: 1.5px;
        }

        .logo {
            display: grid;
            place-items: center;
            width: 39px;
            height: 39px;
            border: 1px solid rgba(98,168,255,.4);
            border-radius: 12px;
            background: linear-gradient(135deg, #173c70, #10233e);
            color: var(--cyan);
            font-size: 22px;
        }

        .nav-right {
            display: flex;
            align-items: center;
            gap: 24px;
        }

        .nav-right a {
            color: var(--muted);
            text-decoration: none;
            font-size: 13px;
            transition: color .2s;
        }

        .nav-right a:hover {
            color: white;
        }

        .status {
            display: inline-flex;
            align-items: center;
            gap: 9px;
            padding: 9px 13px;
            border: 1px solid rgba(66, 220, 158, .22);
            border-radius: 30px;
            background: rgba(30, 160, 105, .08);
            color: #73e9b4;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .6px;
        }

        .dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #45e6a2;
            box-shadow: 0 0 12px #45e6a2;
        }

        .hero {
            display: grid;
            grid-template-columns: 1.05fr .95fr;
            gap: 65px;
            align-items: center;
            padding: 95px 0 80px;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 9px;
            padding: 9px 13px;
            margin-bottom: 26px;
            border: 1px solid rgba(98,168,255,.25);
            border-radius: 7px;
            background: rgba(47, 101, 175, .12);
            color: #9ac8ff;
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 1.4px;
        }

        h1 {
            font-size: clamp(43px, 5.3vw, 68px);
            line-height: 1.08;
            letter-spacing: -2.8px;
            font-weight: 800;
        }

        h1 span {
            display: block;
            color: transparent;
            background: linear-gradient(95deg, #72b7ff, #63e9e1);
            background-clip: text;
            -webkit-background-clip: text;
        }

        .subtitle {
            margin-top: 22px;
            color: #dce6f6;
            font-size: 19px;
            line-height: 1.6;
        }

        .description {
            max-width: 470px;
            margin-top: 14px;
            color: var(--muted);
            font-size: 14px;
            line-height: 1.9;
        }

        .buttons {
            display: flex;
            flex-wrap: wrap;
            gap: 13px;
            margin-top: 30px;
        }

        .btn {
            display: inline-flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            padding: 14px 19px;
            border: 1px solid var(--border);
            border-radius: 9px;
            color: #dce9fc;
            background: rgba(255,255,255,.035);
            text-decoration: none;
            font-size: 13px;
            font-weight: 700;
            transition: transform .2s, border-color .2s;
        }

        .btn:hover {
            transform: translateY(-3px);
            border-color: var(--blue);
        }

        .btn-primary {
            color: #07111f;
            border-color: transparent;
            background: linear-gradient(100deg, #8dc3ff, #70e5e0);
        }

        .pipeline {
            position: relative;
            padding: 26px;
            border: 1px solid rgba(131, 164, 218, .22);
            border-radius: 20px;
            background: linear-gradient(
                145deg, rgba(24, 38, 65, .9),
                rgba(12, 20, 37, .85)
            );
            box-shadow: 0 25px 80px rgba(0,0,0,.25);
        }

        .panel-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 20px;
            border-bottom: 1px solid var(--border);
        }

        .panel-title {
            font-size: 13px;
            font-weight: 700;
        }

        .panel-subtitle {
            margin-top: 6px;
            color: var(--muted);
            font-size: 11px;
        }

        .live {
            color: #70e9b2;
            font-size: 10px;
            letter-spacing: 1px;
        }

        .pipeline-steps {
            padding-top: 25px;
        }

        .step {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 16px;
            border: 1px solid var(--border);
            border-radius: 12px;
            background: rgba(255,255,255,.025);
        }

        .step-icon {
            display: grid;
            place-items: center;
            flex-shrink: 0;
            width: 43px;
            height: 43px;
            border-radius: 11px;
            background: rgba(83, 229, 223, .09);
            font-size: 20px;
        }

        .step:nth-of-type(3) .step-icon {
            background: rgba(98, 168, 255, .12);
        }

        .step-name {
            font-size: 13px;
            font-weight: 750;
        }

        .step-desc {
            margin-top: 5px;
            color: var(--muted);
            font-size: 11px;
        }

        .check {
            margin-left: auto;
            color: #63e5ad;
            font-size: 18px;
        }

        .connector {
            width: 2px;
            height: 21px;
            margin-left: 37px;
            background: linear-gradient(var(--cyan), var(--blue));
            opacity: .65;
        }

        .pipeline-footer {
            display: flex;
            justify-content: space-between;
            gap: 10px;
            margin-top: 22px;
            padding-top: 17px;
            border-top: 1px solid var(--border);
            color: var(--muted);
            font-size: 10px;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
            padding-bottom: 65px;
        }

        .feature {
            padding: 24px;
            border: 1px solid var(--border);
            border-radius: 14px;
            background: rgba(16, 25, 44, .62);
            transition: transform .25s, border-color .25s;
        }

        .feature:hover {
            transform: translateY(-5px);
            border-color: rgba(98,168,255,.5);
        }

        .feature-number {
            color: var(--cyan);
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 1.3px;
        }

        .feature h2 {
            margin-top: 17px;
            font-size: 17px;
        }

        .feature p {
            margin-top: 10px;
            color: var(--muted);
            font-size: 12px;
            line-height: 1.8;
        }

        footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 15px;
            padding: 22px 0 28px;
            border-top: 1px solid var(--border);
            color: var(--muted);
            font-size: 11px;
        }

        .footer-status {
            display: flex;
            align-items: center;
            gap: 8px;
            color: #75e9b6;
        }

        @media (max-width: 800px) {
            .hero {
                grid-template-columns: 1fr;
                gap: 40px;
                padding: 65px 0;
            }

            .features {
                grid-template-columns: 1fr;
            }

            .nav-right a {
                display: none;
            }

            h1 {
                letter-spacing: -1.7px;
            }
        }

        @media (max-width: 420px) {
            .container {
                width: 92%;
            }

            .pipeline {
                padding: 16px;
            }

            .status {
                padding: 8px;
                font-size: 9px;
            }

            footer {
                align-items: flex-start;
                flex-direction: column;
            }
        }
    </style>
</head>

<body>
    <div class="container">
        <nav>
            <div class="brand">
                <div class="logo">⌘</div>
                <span>HELLO CLOUD</span>
            </div>

            <div class="nav-right">
                <a href="#platform">Platform</a>
                <a href="#pipeline">Pipeline</a>
                <a href="#about">About</a>
                <div class="status">
                    <span class="dot"></span>
                    SYSTEM ONLINE
                </div>
            </div>
        </nav>

        <main>
            <section class="hero" id="platform">
                <div class="hero-content">
                    <div class="eyebrow">
                        <span>✦</span>
                        DEPLOYED WITH JENKINS
                    </div>

                    <h1>
                        From Code
                        <span>to Cloud.</span>
                    </h1>

                    <p class="subtitle">
                        A simple Python app. A real CI/CD workflow.
                    </p>

                    <p class="description">
                        Built with Flask, containerized with Docker,
                        and delivered through a Jenkins pipeline.
                        One step at a time, from source code to a
                        running application.
                    </p>

                    <div class="buttons">
                        <a class="btn btn-primary"
                           href="#pipeline">
                            Explore the Pipeline <span>→</span>
                        </a>
                        <a class="btn" href="#about">
                            Discover the Stack ↗
                        </a>
                    </div>
                </div>

                <div class="pipeline" id="pipeline">
                    <div class="panel-header">
                        <div>
                            <div class="panel-title">
                                Deployment Pipeline
                            </div>
                            <div class="panel-subtitle">
                                Application delivery workflow
                            </div>
                        </div>
                        <div class="live">● DEMO</div>
                    </div>

                    <div class="pipeline-steps">
                        <div class="step">
                            <div class="step-icon">⌘</div>
                            <div>
                                <div class="step-name">Source Code</div>
                                <div class="step-desc">
                                    Python · Git Repository
                                </div>
                            </div>
                            <div class="check">✓</div>
                        </div>

                        <div class="connector"></div>

                        <div class="step">
                            <div class="step-icon">▣</div>
                            <div>
                                <div class="step-name">Build & Package</div>
                                <div class="step-desc">
                                    Docker · Container Image
                                </div>
                            </div>
                            <div class="check">✓</div>
                        </div>

                        <div class="connector"></div>

                        <div class="step">
                            <div class="step-icon">⇧</div>
                            <div>
                                <div class="step-name">CI/CD Pipeline</div>
                                <div class="step-desc">
                                    Jenkins · Automated Workflow
                                </div>
                            </div>
                            <div class="check">✓</div>
                        </div>
                    </div>

                    <div class="pipeline-footer">
                        <span>ENVIRONMENT: LAB</span>
                        <span>STACK: PYTHON + DEVOPS</span>
                    </div>
                </div>
            </section>

            <section class="features" id="about">
                <article class="feature">
                    <div class="feature-number">01 / BUILD</div>
                    <h2>Build with Purpose</h2>
                    <p>
                        Package a Python application into a
                        portable Docker image for consistent
                        environments.
                    </p>
                </article>

                <article class="feature">
                    <div class="feature-number">02 / AUTOMATE</div>
                    <h2>Automate the Workflow</h2>
                    <p>
                        Use Jenkins to orchestrate pipeline stages
                        and make software delivery repeatable.
                    </p>
                </article>

                <article class="feature">
                    <div class="feature-number">03 / DEPLOY</div>
                    <h2>Deliver with Confidence</h2>
                    <p>
                        Run a containerized web application and
                        validate the result in a browser.
                    </p>
                </article>
            </section>
        </main>

        <footer>
            <div class="footer-status">
                <span class="dot"></span>
                APPLICATION RESPONDING
            </div>
            <div>FLASK · DOCKER · JENKINS</div>
            <div>PORT 5000 · DEVOPS LAB</div>
        </footer>
    </div>
</body>
</html>
"""


@app.route("/")
def hello_world():
    return render_template_string(PAGE)


@app.route("/health")
def health():
    return {"status": "ok", "application": "hello-cloud"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
