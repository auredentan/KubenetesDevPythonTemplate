import * as React from "react";
import { test } from "../services/fetch";

export interface HelloProps {
    compiler: string;
    framework: string;
}

export const Hello = (props: HelloProps) => {
    return (
        <div>
            <h1>
                Hello from {props.compiler} and {props.framework}!
            </h1>
            <button onClick={() => {
                test().then((r) => console.log(r))
                }}>Hello Cliick he </button>
        </div>
    );
};
