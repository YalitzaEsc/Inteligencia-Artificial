import java.util.*;

public class BreadthFirstSearch {
    private Node root;
    private String goalState;

    public BreadthFirstSearch(Node root, String goalState) {
        this.root = root;
        this.goalState = goalState;
    }

    public void search() {
        Set<String> visitedStates = new HashSet<>();
        Node node = new Node(root.getState());
        Queue<Node> queue = new LinkedList<>();
        Node currentNode = node;
        
        while (!currentNode.getState().equals(goalState)) {
            visitedStates.add(currentNode.getState());
            List<String> nodeSuccessors = NodeUtil.getSuccessors(currentNode.getState());
            
            for (String successor : nodeSuccessors) {
                if (!visitedStates.contains(successor)) {
                    visitedStates.add(successor);
                    Node child = new Node(successor);
                    currentNode.addChild(child);
                    child.setParent(currentNode);
                    queue.add(child);
                }
            }
            currentNode = queue.poll();
        }
        NodeUtil.printSolution(currentNode, visitedStates, root);
    }
}
