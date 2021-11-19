FROM mcr.microsoft.com/dotnet/core/runtime:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src
COPY ["ImplementingDoubledLinkedList/ImplementingDoubledLinkedList.csproj", "ImplementingDoubledLinkedList/"]
RUN dotnet restore "ImplementingDoubledLinkedList/ImplementingDoubledLinkedList.csproj"
COPY . .
WORKDIR "/src/ImplementingDoubledLinkedList"
RUN dotnet build "ImplementingDoubledLinkedList.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "ImplementingDoubledLinkedList.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ImplementingDoubledLinkedList.dll"]
