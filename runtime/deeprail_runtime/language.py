
SUPPORTED = {"ja", "en"}

def resolve_language(profile):
    dr = profile["deeprail"]
    lang = dr.get("language", {})
    communication = lang.get("communication", "ja")
    artifacts = lang.get("artifacts", "ja")
    for value, field in [(communication, "communication"), (artifacts, "artifacts")]:
        if value not in SUPPORTED:
            raise ValueError(f"Unsupported {field} language: {value}")
    return {
        "communication_language": communication,
        "artifact_output_language": artifacts,
    }

def runtime_language_instruction(resolved):
    labels = {"ja": "Japanese", "en": "English"}
    c = labels[resolved["communication_language"]]
    a = labels[resolved["artifact_output_language"]]
    return f"""Communication language: {c}
Artifact output language: {a}

Use the communication language for all human-facing interaction.
Use the artifact output language for human-readable generated artifacts.
Do not translate Stable Module IDs, schema property names, code identifiers,
protocol constants, command names, or machine-readable enum values."""
