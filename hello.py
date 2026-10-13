from flask import Flask, render_template_string

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#0c0a14">
    <title>DevOps Control Center</title>

    <style>
        :root {
            --bg: #0c0a14;
            --panel: #15121f;
            --purple: #a78bfa;
            --pink: #f0abfc;
            --green: #86efac;
            --text: #f5f3ff;
            --muted: #a5a0b5;
            --border: #292437;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            color: var(--text);
            font-family: Inter, "Segoe UI", Arial, sans-serif;
            background:
                radial-gradient(circle at 85% 5%,
                    rgba(139, 92, 246, .15), transparent 30%),
                radial-gradient(circle at 5% 75%,
                    rgba(217, 70, 239, .08), transparent 28%),
                var(--bg);
        }

        a {
            color: inherit;
            text-decoration: none;
        }

        .container {
            width: min(1120px, 90%);
            margin: auto;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 25px 0;
            border-bottom: 1px solid var(--border);
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 15px;
            font-weight: 800;
            letter-spacing: 1px;
        }

        .brand-icon {
            display: grid;
            place-items: center;
            width: 42px;
            height: 42px;
            border-radius: 13px;
            color: #160d26;
            background: linear-gradient(135deg, var(--purple), var(--pink));
            font-size: 23px;
        }

        .header-tag {
            padding: 9px 13px;
            border: 1px solid #315d43;
            border-radius: 30px;
            color: var(--green);
            background: rgba(34, 197, 94, .07);
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .5px;
        }

        .hero {
            padding: 75px 0 38px;
        }

        .eyebrow {
            color: var(--pink);
            font-size: 11px;
            font-weight: 800;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        h1 {
            max-width: 760px;
            margin-top: 18px;
            font-size: clamp(38px, 6vw, 66px);
            line-height: 1.08;
            letter-spacing: -2px;
        }

        h1 span {
            color: var(--purple);
        }

        .hero p {
            max-width: 620px;
            margin-top: 20px;
            color: var(--muted);
            font-size: 16px;
            line-height: 1.9;
        }

        .section-heading {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 15px;
            margin: 32px 0 18px;
        }

        .section-heading h2 {
            font-size: 18px;
        }

        .section-heading span {
            color: var(--muted);
            font-size: 12px;
        }

        .stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 18px;
        }

        .stat {
            padding: 23px;
            border: 1px solid var(--border);
            border-radius: 16px;
            background: linear-gradient(145deg, #191525, #12101a);
        }

        .stat-label {
            color: var(--muted);
            font-size: 12px;
        }

        .stat-value {
            margin-top: 15px;
            font-size: 30px;
            font-weight: 800;
        }

        .stat-note {
            margin-top: 9px;
            color: var(--green);
            font-size: 11px;
        }

        .workspace {
            display: grid;
            grid-template-columns: 1.2fr .8fr;
            gap: 20px;
            margin: 24px 0 70px;
        }

        .panel {
            padding: 25px;
            border: 1px solid var(--border);
            border-radius: 17px;
            background: rgba(21, 18, 31, .88);
        }

        .panel h2 {
            font-size: 16px;
        }

        .panel-description {
            margin-top: 8px;
            color: var(--muted);
            font-size: 12px;
            line-height: 1.7;
        }

        .pipeline {
            margin-top: 25px;
        }

        .pipeline-item {
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 15px 0;
            border-bottom: 1px solid var(--border);
        }

        .pipeline-item:last-child {
            border-bottom: none;
        }

        .step-number {
            display: grid;
            place-items: center;
            width: 38px;
            height: 38px;
            flex-shrink: 0;
            border-radius: 11px;
            color: var(--purple);
            background: rgba(167, 139, 250, .12);
            font-size: 12px;
            font-weight: 800;
        }

        .step-info {
            flex: 1;
        }

        .step-info strong {
            font-size: 13px;
        }

        .step-info p {
            margin-top: 5px;
            color: var(--muted);
            font-size: 11px;
        }

        .step-status {
            color: var(--green);
            font-size: 10px;
            font-weight: 800;
        }

        .branch {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-top: 17px;
            padding: 15px;
            border: 1px solid var(--border);
            border-radius: 12px;
            background: rgba(255, 255, 255, .02);
        }

        .branch-symbol {
            color: var(--purple);
            font-size: 19px;
        }

        .branch-info {
            flex: 1;
        }

        .branch-info strong {
            font-size: 13px;
        }

        .branch-info p {
            margin-top: 5px;
            color: var(--muted);
            font-size: 11px;
        }

        .branch-label {
            padding: 5px 8px;
            border-radius: 6px;
            background: rgba(167, 139, 250, .12);
            color: var(--purple);
            font-size: 10px;
            font-weight: 800;
        }

        .callout {
            margin-top: 22px;
            padding: 17px;
            border: 1px solid #403052;
            border-radius: 12px;
            background: rgba(167, 139, 250, .06);
        }

        .callout strong {
            font-size: 12px;
            color: var(--pink);
        }

        .callout p {
            margin-top: 8px;
            color: var(--muted);
            font-size: 12px;
            line-height: 1.8;
        }

        footer {
            display: flex;
            justify-content: space-between;
            gap: 15px;
            padding: 23px 0;
            border-top: 1px solid var(--border);
            color: var(--muted);
            font-size: 11px;
        }

        footer span {
            color: var(--purple);
        }

        @media (max-width: 760px) {
            .stats {
                grid-template-columns: 1fr;
            }

            .workspace {
                grid-template-columns: 1fr;
            }

            .hero {
                padding-top: 55px;
            }

            h1 {
                letter-spacing: -1px;
            }

            footer {
                flex-direction: column;
            }
        }
    </style>
</head>

<body>
    <div class="container">
        <header>
            <a class="brand" href="/">
                <div class="brand-icon">⌘</div>
                <span>DEVOPS / CONTROL</span>
            </a>
            <div class="header-tag">● LAB ENVIRONMENT</div>
        </header>

        <main>
            <section class="hero">
                <div class="eyebrow">Automation workspace / 001</div>

                <h1>
                    Ship smarter.<br>
                    <span>Deploy with confidence.</span>
                </h1>

                <p>
                    A hands-on DevOps project exploring automated builds,
                    Docker containerization, and Jenkins multibranch pipelines.
                    From source control to a running application.
                </p>
            </section>

            <section>
                <div class="section-heading">
                    <h2>Platform Overview</h2>
                    <span>Project dashboard</span>
                </div>

                <div class="stats">
                    <article class="stat">
                        <div class="stat-label">APPLICATION</div>
                        <div class="stat-value">Flask</div>
                        <div class="stat-note">● Python web service</div>
                    </article>

                    <article class="stat">
                        <div class="stat-label">CONTAINER ENGINE</div>
                        <div class="stat-value">Docker</div>
                        <div class="stat-note">● Containerized delivery</div>
                    </article>

                    <article class="stat">
                        <div class="stat-label">AUTOMATION</div>
                        <div class="stat-value">Jenkins</div>
                        <div class="stat-note">● Pipeline as code</div>
                    </article>
                </div>
            </section>

            <section class="workspace">
                <article class="panel">
                    <h2>Delivery Workflow</h2>
                    <p class="panel-description">
                        The stages used to package and run the application.
                    </p>

                    <div class="pipeline">
                        <div class="pipeline-item">
                            <div class="step-number">01</div>
                            <div class="step-info">
                                <strong>Source Control</strong>
                                <p>Git repository and branch discovery</p>
                            </div>
                            <div class="step-status">SOURCE</div>
                        </div>

                        <div class="pipeline-item">
                            <div class="step-number">02</div>
                            <div class="step-info">
                                <strong>Build Image</strong>
                                <p>Dockerfile and image creation</p>
                            </div>
                            <div class="step-status">BUILD</div>
                        </div>

                        <div class="pipeline-item">
                            <div class="step-number">03</div>
                            <div class="step-info">
                                <strong>Pipeline Execution</strong>
                                <p>Jenkins automated stages</p>
                            </div>
                            <div class="step-status">CI/CD</div>
                        </div>

                        <div class="pipeline-item">
                            <div class="step-number">04</div>
                            <div class="step-info">
                                <strong>Container Runtime</strong>
                                <p>Run the application in Docker</p>
                            </div>
                            <div class="step-status">RUN</div>
                        </div>
                    </div>
                </article>

                <aside class="panel">
                    <h2>Branch Strategy</h2>
                    <p class="panel-description">
                        Separate branches can trigger independent Jenkins jobs.
                    </p>

                    <div class="branch">
                        <div class="branch-symbol">⑂</div>
                        <div class="branch-info">
                            <strong>dev</strong>
                            <p>Development workflow</p>
                        </div>
                        <div class="branch-label">DEV</div>
                    </div>

                    <div class="branch">
                        <div class="branch-symbol">⑂</div>
                        <div class="branch-info">
                            <strong>stg</strong>
                            <p>Staging workflow</p>
                        </div>
                        <div class="branch-label">STG</div>
                    </div>

                    <div class="branch">
                        <div class="branch-symbol">⑂</div>
                        <div class="branch-info">
                            <strong>prod</strong>
                            <p>Production workflow</p>
                        </div>
                        <div class="branch-label">PROD</div>
                    </div>

                    <div class="callout">
                        <strong>ENGINEERING NOTE</strong>
                        <p>
                            This dashboard describes the lab workflow.
                            Check Jenkins Console Output to verify the
                            actual status of each pipeline execution.
                        </p>
                    </div>
                </aside>
            </section>
        </main>

        <footer>
            <div>DEVOPS CONTROL CENTER <span>v1.0</span></div>
            <div>FLASK · DOCKER · JENKINS</div>
            <div>APPLICATION PORT: 5000</div>
        </footer>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE)


@app.route("/health")
def health():
    return {
        "status": "ok",
        "application": "devops-control-center"
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
