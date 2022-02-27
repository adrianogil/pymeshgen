
if [ -z "$PYMESHGEN_PYTHON_PATH" ]
then
    export PYMESHGEN_PYTHON_PATH=$PYMESHGEN_PROJ_PATH/python
    export PYTHONPATH=$PYMESHGEN_PYTHON_PATH:$PYTHONPATH
fi

function pymeshgen-generate()
{
    python3 -m meshgen.generate
}