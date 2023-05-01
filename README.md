# MLOps 

## Machine Learning Operations

Model creation must be

> - scalable
> - collaborative
> - reproduceble

### DataOps

> Set of rules that ensure a high quality of data to train models


### MLOps addresses to

> - Versioning
> - Model Tracking
> - Feature Generation


### MLOps (ML + Dev + Ops)

- ML (Experiment)
    - Data Acquisition
    - Business Undertanding
    - Initial Modeling

- Develop
    - Modeling + Testing
    - Continuous Integration
    - Continuous Deployment

- Operate
    - Continuous Delivery
    - Data Feedback Loop
    - System + Model Monitoring    
    - Continuous Training

### MLOps Process

#### Use Case Discorevy

- Business Understanding
- Use Case Identification
- Data Understanding
- Feasibility Study

#### Data Engineering

- Data Preparation

#### ML Pipeline

- Learning Algorithms
- Model Building/Training
- Model Experimentation
- Model Evaluation
- Model Serving

#### Production Deployment

- Deploy
- Automate

#### Production Monitoring

- Operate
- Monitor
- Optimize


### MLOps Parts [CRISP-ML]

<table>
<tr>
    <th>Part</th>
    <th>Objective</th>
    <th>Software</th>
</tr>
<tr>
    <td>Feature Store</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>Data Versioning</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>Metadata Store</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>Model Versioning</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>Model Registration</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>Model Serving</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>Model Monitoring</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>Recycling of models</td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>CI/CD</td>
    <td></td>
    <td></td>
</tr>
</table>

![CRISP-ML-FIGURE](https://ml-ops.org/img/crisp-ml-process.jpg)

### MLOps Stages

<table>
<tr>
    <th>Stage</th>
    <th>Definition</th>    
</tr>
<tr>
    <td>Stage 1</td>
    <td>Model and Data <b>Version Control</b></td>
</tr>
<tr>
    <td>Stage 2</td>
    <td><b>AutoML</b> + Model and Data Version Control</td>    
</tr>
<tr>
    <td>Stage 3</td>
    <td>AutoML + Model and Data Version Control + <b>Model Serving</b></td>   
</tr>
<tr>
    <td>Stage 4</td>
       <td>AutoML + Model and Data Version Control + Model Serving + <b>Monitoring, Governance and Retraining (Fig 2)</b></td>   
</tr>
</table>

![Continuous Training](https://ml-ops.org/img/model-decay-monitoring.jpg)
<figcaption>Fig 2 - Continuous Training</figcaption>

## Installing

### Tools and Libraries

- Libraries
- Jupyter Notebook
- Docker

### Tips

Jupyter Notebook environment (Conda)

```sh
    $ conda install -n [env] ipykernel
    $ python -m ipykernel install --user --name [env] --display-name "Python (mlops)"
```




## References

- [Landscape AI Infrastructure]
- [Jupyter Notebook Template]


[Landscape AI Infrastructure]: https://ai-infrastructure.org/ai-infrastructure-landscape/

[Jupyter Notebook Template]: https://github.com/acnaweb/notebook

[CRISP-ML]: https://ml-ops.org/content/crisp-ml


