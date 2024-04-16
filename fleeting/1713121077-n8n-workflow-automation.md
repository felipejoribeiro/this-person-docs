---
id: 1713121077-n8n-workflow-automation
aliases:
  - n8n-workflow-automation
tags: []
---

# N8N: Workflow Automation

<span style="text-align: center; width: 100%; font-size: 0.75em; margin-bottom: 20px">
    A guide to the N8N platform, a powerful tool for workflow automation, integration, and orchestration.
</span>

![circuit-header.png](../assets/from_notes/1713121077-n8n-workflow-automation-2024-04-14-17-00-08-circuit-header.png)

## ✾ Introduction

**N8N** is a service that allows the user to automate workflows. It has a no-code approach, with integration to a variaty of services and applications. The softawre is open-source and it is available for free on [github](https://github.com/n8n-io/n8n). It can be deployed and run on your own infrastructure:

![n8n-interface-home.png](../assets/from_notes/1713121077-n8n-workflow-automation-2024-04-15-11-56-30-n8n-interface-home.png)

Here is an example of a workflow in the **N8N** interface:

![example-workflow.png](../assets/from_notes/1713121077-n8n-workflow-automation-2024-04-15-12-44-24-example-workflow.png)

The interface is great, and the node-bsed approach is very intuitive. The user can create complex workflows with a few clicks.

## ✾ Installation

To install the tool you can use the `npx n8n` command. It will download the package if it is not already installed and it will start the service. The `node` version required to run the software is `18` or higher. After initialization, the service will be available at [http://localhost:5678/](http://localhost:5678/) and the following message will appear:

```
Editor is now accessible via:
http://localhost:5678/
```

## ✾ Workflow

We can imagine the **N8N** service as a circuit board. Each node is a component that can be connected to others. These connections alongside the nodes define the workflow. The first node is the trigger, and it will make the workflow run with input data. The subsequent nodes can process this data, transform it, send it to other services and perform a variety of other actions.

Some interesting nodes are:

- **HTTP REQUEST**: It can make requests to APIs and other services.
- **CODE**: It can run custom JavaScript or python code.
- **GMAIL**: It can send emails using a Gmail account.
- **X(Formerly Twitter)**: It can send tweets and interact with the Twitter API.
- **N8N**: It can interact with the N8N API.

There are a lot of other nodes available, and you can create your own custom nodes if needed.
To create a custom node you can use the `npx n8n-node-dev` command. It will create a new node in the `packages/nodes-base/nodes` folder. You can then edit the node and add your own logic to it. Reading other nodes code can be a good way to understand how to create your own. Here is an example of a simple custom node:

```typescript
import { IExecuteFunctions } from "n8n-core";
import {
  INodeExecutionData,
  INodeType,
  INodeTypeDescription,
} from "n8n-workflow";

export class MyNode implements INodeType {
  description: INodeTypeDescription = {
    displayName: "My Node",
    name: "myNode",
    group: ["transform"],
    version: 1,
    description: 'Adds "myString" on all items to defined value.',
    defaults: {
      name: "My Node",
      color: "#772244",
    },
    inputs: ["main"],
    outputs: ["main"],
    properties: [
      {
        displayName: "My String",
        name: "myString",
        type: "string",
        default: "",
        placeholder: "Placeholder value",
        description: "The description text",
      },
    ],
  };
  async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
    const items = this.getInputData();

    let item: INodeExecutionData;
    let myString: string;

    for (let itemIndex = 0; itemIndex < items.length; itemIndex++) {
      myString = this.getNodeParameter("myString", itemIndex, "") as string;
      item = items[itemIndex];

      item.json["myString"] = myString;
    }

    return this.prepareOutputData(items);
  }
}
```

After creating the node you can use it in your workflows. The node will be available in the editor and you can connect it to other nodes.

## ✾ LLM Integration

The **N8N** service has [langchain](1713196132-langchain-llm-applications.md) integration with [large-language-models](1712254150-large-language-models.md) services. You can use the **AI** node to interact with these services. Therefore, the **AI** node can be used to perform a variety of tasks, such as text generation, translation, and summarization.

Simple example of a workflow that uses the AI nodes to connect to OpenAI's **GPT-3.5** service:

![llm-n8n-chart-basic.png](../assets/from_notes/1713121077-n8n-workflow-automation-2024-04-15-11-30-57-llm-n8n-chart-basic.png)

Here is another example, but with an AI agent. This agent can remember the user's previous prompts, use a calculator and search for information on Wikipedia:

![example-workflow-calculator-wikipedia.png](../assets/from_notes/1713121077-n8n-workflow-automation-2024-04-15-17-31-19-example-workflow-calculator-wikipedia.png)

Remember that.
