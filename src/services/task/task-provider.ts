import db from "../../config/db";
import { LooseObject } from "../../utils/models";

export const createTask = async (params: LooseObject) => {
    return await db.one(
        'INSERT INTO public."Tasks"( user_id, command) VALUES ( ${user_id}, ${command}) returning id',
        params);
};