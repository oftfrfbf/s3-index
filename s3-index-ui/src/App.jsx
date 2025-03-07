import React from 'react';
import ForceGraph2D from 'react-force-graph-2d';
import gD from './data/data.json';
import SpriteText from 'three-spritetext';

function App() {

    // const numNodes = 300;
    // const nodes = [...Array(numNodes)].map((_, index) => ({ id: `Node ${index + 1}` }));
    // // Sample data for the graph
    // const graphData = {
    //     nodes: nodes,
    //     links: [
    //         { source: 'Node 1', target: 'Node 2' },
    //         { source: 'Node 2', target: 'Node 3' },
    //         // Add more links as needed
    //     ],
    // };
    // debugger;
    const graphData = {
        nodes: gD.nodes,
        links: gD.links,
    };

    return (
        <div>
            <ForceGraph2D
                graphData={graphData}
                nodeAutoColorBy="id"
                // nodeThreeObject={node => {
                //   const sprite = new SpriteText(node.id);
                //   sprite.color = node.color;
                //   sprite.textHeight = 8;
                //   return sprite;
                // }}
                nodeCanvasObject={(node, ctx, globalScale) => {
                    const label = node.id;
                    const fontSize = 12/globalScale;
                    ctx.font = `${fontSize}px Sans-Serif`;
                    const textWidth = ctx.measureText(label).width;
                    const bckgDimensions = [textWidth, fontSize].map(n => n + fontSize * 0.2); // some padding

                    ctx.fillStyle = 'rgba(255, 255, 255, 0.8)';
                    ctx.fillRect(node.x - bckgDimensions[0] / 2, node.y - bckgDimensions[1] / 2, ...bckgDimensions);

                    ctx.textAlign = 'center';
                    ctx.textBaseline = 'middle';
                    ctx.fillStyle = node.color;
                    ctx.fillText(`${label}`, node.x, node.y);

                    node.__bckgDimensions = bckgDimensions; // to re-use in nodePointerAreaPaint
                }}
                nodePointerAreaPaint={(node, color, ctx) => {
                    ctx.fillStyle = color;
                    const bckgDimensions = node.__bckgDimensions;
                    bckgDimensions && ctx.fillRect(node.x - bckgDimensions[0] / 2, node.y - bckgDimensions[1] / 2, ...bckgDimensions);
                }}
            />
        </div>
    )
}

export default App
