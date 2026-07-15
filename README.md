# Hermes Time Awareness
Simple Hermes plugin to inject current time into the prompt using the `pre_llm_call` hook.

## Install
```sh
mkdir -p ~/.hermes/plugins
git clone https://github.com/Senophyx/hermes-time ~/.hermes/plugins/hermes-time
hermes plugins enable hermes-time
```

## Verify
```sh
hermes -z "What is the current date, time, day of week and timezone? NO TOOLS/TERMINAL USE"
```

## License
```
This Project under MIT License
Copyright (c) 2026 Senophyx
```