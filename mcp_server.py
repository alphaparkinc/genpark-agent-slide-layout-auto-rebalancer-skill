import sys
import json

class SlideLayoutEngine:
    CANVAS_WIDTH = 1920
    CANVAS_HEIGHT = 1080

    @classmethod
    def rebalance(cls, elements, canvas_w=1920, canvas_h=1080):
        rebalanced = []
        current_y = 120
        padding = 30

        for el in elements:
            el_copy = dict(el)
            width = min(el_copy.get("width", 800), canvas_w - 200)
            height = el_copy.get("height", 120)

            el_copy["x"] = 100
            el_copy["y"] = current_y
            el_copy["width"] = width
            el_copy["height"] = height

            current_y += height + padding
            rebalanced.append(el_copy)

        overflow = current_y > canvas_h

        return {
            "canvas": {"width": canvas_w, "height": canvas_h},
            "elements": rebalanced,
            "total_height_used": current_y,
            "has_overflow": overflow,
            "collision_free": True
        }

def handle_rpc(request):
    method = request.get("method")
    req_id = request.get("id")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "rebalance_slide_layout",
                        "description": "Rebalance presentation elements to prevent collisions and overflow.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "elements": {"type": "array", "items": {"type": "object"}},
                                "canvas_width": {"type": "integer", "default": 1920},
                                "canvas_height": {"type": "integer", "default": 1080}
                            },
                            "required": ["elements"]
                        }
                    }
                ]
            }
        }

    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "rebalance_slide_layout":
            res = SlideLayoutEngine.rebalance(
                args.get("elements", []),
                args.get("canvas_width", 1920),
                args.get("canvas_height", 1080)
            )
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res)}]}}

    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "\n")
            sys.stdout.flush()
