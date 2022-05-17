pipeline {
  stage('run tox envs') {
    steps {
      script {
        def envs = sh(returnStdout: true, script: "tox -l").trim().split('\n')
        def cmds = envs.collectEntries({ tox_env ->
          [tox_env, {
            sh "tox --parallel--safe-build -vve $tox_env"
          }]
        })
        parallel(cmds)
      }
    }
  }
}
