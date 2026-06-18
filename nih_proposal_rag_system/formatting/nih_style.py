def format_nih_proposal(aims_output, blueprint_output):
    aims = aims_output["aims"]
    bp = blueprint_output["blueprint"]

    lines = []

    lines.append("SPECIFIC AIMS")
    for i, a in enumerate(aims, start=1):
        lines.append(f"Aim {i}: {a['title']}")
        lines.append(a["description"])
        lines.append("")

    lines.append("SIGNIFICANCE")
    lines.append(bp["significance"])
    lines.append("")

    lines.append("INNOVATION")
    lines.append(bp["innovation"])
    lines.append("")

    lines.append("APPROACH")
    for a in bp["approach"]:
        lines.append(f"Aim: {a['aim']}")
        lines.append(a["plan"])
        lines.append("")

    return "\n".join(lines)