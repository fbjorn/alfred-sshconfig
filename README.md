### Installation

[Download](https://github.com/fbjorn/alfred-sshconfig/releases/) Alfred workflow
and open it

### Usage

Invoke Alfred and type `ssh`

Hosts from `~/.ssh/config` are parsed and prompted to the output. Choose
required one (fuzzy search supported) and press enter.

Alfred will open new tab in iTerm2 and will connect you to the host.

### Local development

```bash
make
```

It will create a `alfred-sshconfig` folder in your default Alfred installation
and add all required source files as symlinks.

Then just open Alfred on Workflows tab and you'll find it.

---

Made with [Alfred-Workflow](https://github.com/deanishe/alfred-workflow)

Bootstrapped from
[alfred-python-template](https://github.com/fbjorn/alfred-python-template)

Icons made by [Freepik](https://www.flaticon.com/authors/freepik) from
[Flaticon](https://www.flaticon.com/)
