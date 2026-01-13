import subprocess
import json

def analyze_pcap_with_cpp(filepath):
    """C++バイナリ analyze を呼んでJSONを返す"""
    try:
        # ./analyze <filepath> がJSON出力する想定
        result = subprocess.run(
            ["./analyze", filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        return {"error": f"C++ analyze failed: {e.stderr}"}
    except json.JSONDecodeError as e:
        return {"error": f"JSON decode failed: {str(e)}", "stdout": result.stdout}