import { Request, Response } from "express";
import * as controller from "./executer-controller";
const axios = require('axios')

export default [
    {
        path: "/Executer/Status",
        method: "post",
        handler: [
          async (req: Request, res: Response) => {
          let statusExecuter = (await axios.get(`http://192.168.40.130:5000/status/${req.body.task_id}`)).data;
          if(statusExecuter["status"] == "SUCCESS")
          {
            //TODO -> return executer task_id from db
            return "shit";
          }
          else
          {
            return statusExecuter;
          }
          }]
        },
        {
          path: "/Executer",
          method: "patch",
          handler: [async (req: Request, res: Response) => {
            let params;
            if(req.body.executer) {
              params = { status: 'RUNNING',
                         step_id: req.body.task_id
                       };
            } else {
              params = { status: req.body.status,
                         step_id: req.body.task_id
                       };
            }
              const data = await controller.Executer(params);
              res.status(200).json(true);
            }
          ]}
];
