import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.Map;
import java.util.HashMap;

import org.json.JSONArray;
import org.json.JSONObject;
import org.graphstream.graph.*;
import org.graphstream.graph.implementations.*;
import org.graphstream.ui.view.Viewer;

public class FSMGraphGenerator {
    public static Graph generateFSMGraph(String fsmTextJson) {
        JSONObject fsm = new JSONObject(fsmTextJson);

        JSONArray states = fsm.getJSONArray("states");
        JSONArray initialStates = fsm.getJSONArray("initialStates");
        JSONArray finalStates = fsm.getJSONArray("finalStates");
        JSONArray transitions = fsm.getJSONArray("transitions");

        // Create a directed graph
        Graph graph = new SingleGraph("FSMGraph");

        // Add states as nodes
        for (Object stateObj : states) {
            String state = (String) stateObj;
            Node node = graph.addNode(state);
            HashMap<String, Boolean> nodeAttributes = new HashMap<>();

            if (initialStates.toList().contains(state)) {
                nodeAttributes.put("initial", true);
            }
            if (finalStates.toList().contains(state)) {
                nodeAttributes.put("final", true);
            }

            Matcher matcher = Pattern.compile("I(\\d+)").matcher(state);
            if (matcher.find()) {
                nodeAttributes.put("external", true);
            }

            if (state.equals("N1")) {
                nodeAttributes.put("open", true);
            }

            if (!initialStates.toList().contains(state) && !finalStates.toList().contains(state) &&
                    !nodeAttributes.containsKey("external") && !nodeAttributes.containsKey("open")) {
                nodeAttributes.put("normal", true);
            }

            node.addAttribute("ui.style", getNodeStyle(nodeAttributes));
        }

        // Add transitions as edges
        for (Object transitionObj : transitions) {
            JSONObject transition = (JSONObject) transitionObj;
            String fromState = transition.getString("from");
            String toState = transition.getString("to");
            String action = transition.getString("actionCalled");

            graph.addEdge(fromState + toState, fromState, toState, true)
                    .addAttribute("ui.label", action);
        }

        return graph;
    }

    private static String getNodeStyle(Map<String, Boolean> attributes) {
        StringBuilder style = new StringBuilder();
        if (attributes.containsKey("initial")) {
            style.append("fill-color: green; ");
        }
        if (attributes.containsKey("final")) {
            style.append("fill-color: red; ");
        }
        if (attributes.containsKey("external")) {
            style.append("fill-color: black; ");
        }
        if (attributes.containsKey("open")) {
            style.append("fill-color: white; ");
        }
        if (attributes.containsKey("normal")) {
            style.append("fill-color: #e5e7eb; ");
        }

        return style.toString();
    }

    public static void drawFSMGraph(Graph graph) {
        graph.addAttribute("ui.stylesheet", "node { size: 20px; }");

        Viewer viewer = graph.display();
        viewer.setCloseFramePolicy(Viewer.CloseFramePolicy.HIDE_ONLY);
    }

    public static String readJsonFile(String filePath) throws IOException {
        byte[] jsonData = Files.readAllBytes(Paths.get(filePath));
        return new String(jsonData);
    }

    public static void main(String[] args) {
        String filePath = "path/to/your/file.json"; // Replace with the actual file path
        try {
            String fsmTextJson = readJsonFile(filePath);
            Graph fsmGraph = generateFSMGraph(fsmTextJson);
            drawFSMGraph(fsmGraph);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
